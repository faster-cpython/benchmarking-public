# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-aarch64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 360 ms: 1.17x slower                                                   |
| docutils       | 2.98 sec                                                              | 3.56 sec: 1.19x slower                                                 |
| html5lib       | 65.1 ms                                                               | 73.3 ms: 1.13x slower                                                  |
| tornado_http   | 136 ms                                                                | 141 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 506 ms: 1.23x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 476 ms: 1.21x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 626 ms: 1.18x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 667 ms: 1.16x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.14x faster                                                 |
| async_tree_io              | 1.41 sec                                                              | 1.25 sec: 1.13x faster                                                 |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 811 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 795 ms: 1.11x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.16x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                   |
| nbody          | 105 ms                                                                | 116 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 252 ms: 1.01x faster                                                   |
| regex_effbot   | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                                  |
| regex_v8       | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                  |
| regex_compile  | 137 ms                                                                | 175 ms: 1.27x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 190 ms: 1.03x faster                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                                   |
| xml_etree_process    | 79.0 ms                                                               | 79.2 ms: 1.00x slower                                                  |
| pickle               | 13.4 us                                                               | 13.6 us: 1.02x slower                                                  |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                 |
| unpickle             | 18.5 us                                                               | 19.7 us: 1.07x slower                                                  |
| json_loads           | 30.7 us                                                               | 32.8 us: 1.07x slower                                                  |
| unpickle_pure_python | 260 us                                                                | 278 us: 1.07x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.61 us: 1.07x slower                                                  |
| pickle_pure_python   | 365 us                                                                | 393 us: 1.08x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                           |

Benchmark hidden because not significant (3): pickle_dict, pickle_list, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.79 ms: 1.05x slower                                                  |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                  |
| django_template | 40.7 ms                                                               | 49.8 ms: 1.22x slower                                                  |
| genshi_text     | 27.4 ms                                                               | 35.2 ms: 1.28x slower                                                  |
| genshi_xml      | 60.6 ms                                                               | 82.2 ms: 1.36x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.21x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo              | 49.6 us                                                               | 37.7 us: 1.32x faster                                                  |
| async_tree_none            | 624 ms                                                                | 506 ms: 1.23x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 476 ms: 1.21x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 626 ms: 1.18x faster                                                   |
| deepcopy                   | 446 us                                                                | 381 us: 1.17x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 667 ms: 1.16x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.14x faster                                                 |
| async_tree_io              | 1.41 sec                                                              | 1.25 sec: 1.13x faster                                                 |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 811 ms: 1.12x faster                                                   |
| generators                 | 43.5 ms                                                               | 38.8 ms: 1.12x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 22.1 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 795 ms: 1.11x faster                                                   |
| comprehensions             | 25.4 us                                                               | 23.1 us: 1.10x faster                                                  |
| raytrace                   | 353 ms                                                                | 324 ms: 1.09x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.32 us: 1.04x faster                                                  |
| logging_format             | 8.34 us                                                               | 8.02 us: 1.04x faster                                                  |
| xml_etree_parse            | 195 ms                                                                | 190 ms: 1.03x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                                   |
| regex_dna                  | 254 ms                                                                | 252 ms: 1.01x faster                                                   |
| xml_etree_process          | 79.0 ms                                                               | 79.2 ms: 1.00x slower                                                  |
| mdp                        | 3.41 sec                                                              | 3.44 sec: 1.01x slower                                                 |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                   |
| pickle                     | 13.4 us                                                               | 13.6 us: 1.02x slower                                                  |
| crypto_pyaes               | 86.6 ms                                                               | 88.0 ms: 1.02x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                 |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                  |
| dask                       | 376 ms                                                                | 385 ms: 1.02x slower                                                   |
| thrift                     | 937 us                                                                | 958 us: 1.02x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.34 ms: 1.02x slower                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 4.21 us: 1.03x slower                                                  |
| sqlite_synth               | 3.77 us                                                               | 3.87 us: 1.03x slower                                                  |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.26 sec: 1.03x slower                                                 |
| fannkuch                   | 443 ms                                                                | 459 ms: 1.04x slower                                                   |
| tornado_http               | 136 ms                                                                | 141 ms: 1.04x slower                                                   |
| meteor_contest             | 112 ms                                                                | 116 ms: 1.04x slower                                                   |
| async_generators           | 491 ms                                                                | 512 ms: 1.04x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 89.2 ms: 1.05x slower                                                  |
| python_startup_no_site     | 8.37 ms                                                               | 8.79 ms: 1.05x slower                                                  |
| richards_super             | 58.5 ms                                                               | 61.4 ms: 1.05x slower                                                  |
| regex_effbot               | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                                  |
| richards                   | 50.9 ms                                                               | 53.8 ms: 1.06x slower                                                  |
| unpickle                   | 18.5 us                                                               | 19.7 us: 1.07x slower                                                  |
| json                       | 5.54 ms                                                               | 5.92 ms: 1.07x slower                                                  |
| json_loads                 | 30.7 us                                                               | 32.8 us: 1.07x slower                                                  |
| unpickle_pure_python       | 260 us                                                                | 278 us: 1.07x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.61 us: 1.07x slower                                                  |
| pickle_pure_python         | 365 us                                                                | 393 us: 1.08x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                  |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                  |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                 |
| sqlglot_parse              | 1.46 ms                                                               | 1.59 ms: 1.09x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 7.66 ms: 1.09x slower                                                  |
| deltablue                  | 4.12 ms                                                               | 4.48 ms: 1.09x slower                                                  |
| asyncio_tcp                | 566 ms                                                                | 617 ms: 1.09x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.01 ms: 1.10x slower                                                  |
| gc_traversal               | 4.40 ms                                                               | 4.85 ms: 1.10x slower                                                  |
| nbody                      | 105 ms                                                                | 116 ms: 1.11x slower                                                   |
| pyflate                    | 559 ms                                                                | 619 ms: 1.11x slower                                                   |
| scimark_fft                | 418 ms                                                                | 463 ms: 1.11x slower                                                   |
| logging_silent             | 127 ns                                                                | 141 ns: 1.11x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.90 ms: 1.11x slower                                                  |
| html5lib                   | 65.1 ms                                                               | 73.3 ms: 1.13x slower                                                  |
| spectral_norm              | 131 ms                                                                | 147 ms: 1.13x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 69.2 ms: 1.13x slower                                                  |
| go                         | 157 ms                                                                | 178 ms: 1.13x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 144 ms: 1.14x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                  |
| pylint                     | 355 ms                                                                | 410 ms: 1.16x slower                                                   |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                   |
| sympy_str                  | 280 ms                                                                | 326 ms: 1.16x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 72.4 ms: 1.17x slower                                                  |
| 2to3                       | 308 ms                                                                | 360 ms: 1.17x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 212 us: 1.17x slower                                                   |
| scimark_sor                | 150 ms                                                                | 178 ms: 1.19x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.1 ms: 1.19x slower                                                  |
| docutils                   | 2.98 sec                                                              | 3.56 sec: 1.19x slower                                                 |
| nqueens                    | 99.2 ms                                                               | 119 ms: 1.20x slower                                                   |
| sympy_expand               | 454 ms                                                                | 543 ms: 1.20x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 187 ms: 1.21x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.32 ms: 1.21x slower                                                  |
| django_template            | 40.7 ms                                                               | 49.8 ms: 1.22x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 26.5 ms: 1.23x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.12 sec: 1.23x slower                                                 |
| pprint_pformat             | 1.88 sec                                                              | 2.35 sec: 1.25x slower                                                 |
| chaos                      | 71.4 ms                                                               | 89.5 ms: 1.25x slower                                                  |
| scimark_lu                 | 146 ms                                                                | 183 ms: 1.26x slower                                                   |
| regex_compile              | 137 ms                                                                | 175 ms: 1.27x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 35.2 ms: 1.28x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 8.96 ms: 1.28x slower                                                  |
| genshi_xml                 | 60.6 ms                                                               | 82.2 ms: 1.36x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                           |

Benchmark hidden because not significant (6): float, pickle_dict, coroutines, pickle_list, asyncio_websockets, xml_etree_generate
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240618-3.14.0a0-a1bdb94-JIT/bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x