# Results vs. 3.12.0

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: linux-aarch64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.04x faster
- HPT reliability: 99.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 294 ms: 1.05x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.07 sec: 1.03x slower                                                  |
| tornado_http   | 136 ms                                                                | 127 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 426 ms: 1.46x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 556 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 417 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 551 ms: 1.34x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 727 ms: 1.25x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.13 sec: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 726 ms: 1.22x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 92.6 ms: 1.01x slower                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 109 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                                    |
| regex_dna      | 254 ms                                                                | 245 ms: 1.04x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.81 ms: 1.04x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 146 ms: 1.03x faster                                                    |
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 357 us: 1.02x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 77.5 ms: 1.02x faster                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                                  |
| json_loads           | 30.7 us                                                               | 32.2 us: 1.05x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.79 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 59.1 ms: 1.02x faster                                                   |
| django_template | 40.7 ms                                                               | 42.0 ms: 1.03x slower                                                   |
| mako            | 12.9 ms                                                               | 13.6 ms: 1.06x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 426 ms: 1.46x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 556 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 417 ms: 1.38x faster                                                    |
| deepcopy                   | 446 us                                                                | 329 us: 1.36x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 551 ms: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.6 us: 1.32x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 727 ms: 1.25x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.3 us: 1.25x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.13 sec: 1.25x faster                                                  |
| generators                 | 43.5 ms                                                               | 35.1 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 726 ms: 1.22x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 3.45 us: 1.19x faster                                                   |
| raytrace                   | 353 ms                                                                | 300 ms: 1.18x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.3 ms: 1.15x faster                                                   |
| logging_simple             | 7.63 us                                                               | 6.93 us: 1.10x faster                                                   |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 141 ms: 1.10x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 134 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.69 us: 1.08x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.70 ms: 1.07x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.22 ms: 1.07x faster                                                   |
| sympy_str                  | 280 ms                                                                | 262 ms: 1.07x faster                                                    |
| tornado_http               | 136 ms                                                                | 127 ms: 1.07x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 82.3 ms: 1.05x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.92 ms: 1.05x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.2 ms: 1.05x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 20.6 ms: 1.05x faster                                                   |
| 2to3                       | 308 ms                                                                | 294 ms: 1.05x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.40 ms: 1.05x faster                                                   |
| chaos                      | 71.4 ms                                                               | 68.4 ms: 1.04x faster                                                   |
| regex_dna                  | 254 ms                                                                | 245 ms: 1.04x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 146 ms: 1.03x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.03x faster                                                  |
| genshi_xml                 | 60.6 ms                                                               | 59.1 ms: 1.02x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                  |
| pickle_pure_python         | 365 us                                                                | 357 us: 1.02x faster                                                    |
| pprint_safe_repr           | 916 ms                                                                | 898 ms: 1.02x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 77.5 ms: 1.02x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                                  |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.85 sec: 1.01x faster                                                  |
| nqueens                    | 99.2 ms                                                               | 97.9 ms: 1.01x faster                                                   |
| async_generators           | 491 ms                                                                | 485 ms: 1.01x faster                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 6.98 ms: 1.01x faster                                                   |
| thrift                     | 937 us                                                                | 928 us: 1.01x faster                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 61.0 ms: 1.01x faster                                                   |
| float                      | 92.1 ms                                                               | 92.6 ms: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| json                       | 5.54 ms                                                               | 5.59 ms: 1.01x slower                                                   |
| richards_super             | 58.5 ms                                                               | 59.6 ms: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.25 sec: 1.03x slower                                                  |
| docutils                   | 2.98 sec                                                              | 3.07 sec: 1.03x slower                                                  |
| asyncio_tcp                | 566 ms                                                                | 583 ms: 1.03x slower                                                    |
| django_template            | 40.7 ms                                                               | 42.0 ms: 1.03x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.41 ms: 1.03x slower                                                   |
| pyflate                    | 559 ms                                                                | 579 ms: 1.04x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.81 ms: 1.04x slower                                                   |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                    |
| nbody                      | 105 ms                                                                | 109 ms: 1.04x slower                                                    |
| richards                   | 50.9 ms                                                               | 53.1 ms: 1.04x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.79 ms: 1.05x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.2 us: 1.05x slower                                                   |
| scimark_fft                | 418 ms                                                                | 440 ms: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                    |
| fannkuch                   | 443 ms                                                                | 467 ms: 1.05x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.06x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 191 us: 1.06x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| coverage                   | 87.3 ms                                                               | 96.9 ms: 1.11x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.98 ms: 1.13x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.0 ms: 1.18x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.31 ms: 1.21x slower                                                   |
| go                         | 157 ms                                                                | 190 ms: 1.21x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                            |

Benchmark hidden because not significant (9): html5lib, meteor_contest, genshi_text, sympy_expand, hexiom, asyncio_websockets, pylint, xml_etree_generate, sqlglot_normalize
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240827-3.14.0a0-04d5e93/bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93.json: bpe_tokeniser

# HPT report

- Reliability score: 99.77% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x