# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-aarch64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 363 ms: 1.18x slower                                                  |
| docutils       | 2.98 sec                                                              | 3.48 sec: 1.17x slower                                                |
| html5lib       | 65.1 ms                                                               | 71.7 ms: 1.10x slower                                                 |
| tornado_http   | 136 ms                                                                | 143 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 539 ms: 1.37x faster                                                  |
| async_tree_none            | 624 ms                                                                | 473 ms: 1.32x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 448 ms: 1.29x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 604 ms: 1.29x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 764 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 744 ms: 1.19x faster                                                  |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                                |
| async_tree_io_tg           | 1.40 sec                                                              | 1.26 sec: 1.11x faster                                                |
| Geometric mean             | (ref)                                                                 | 1.24x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                  |
| float          | 92.1 ms                                                               | 97.0 ms: 1.05x slower                                                 |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 252 ms: 1.01x faster                                                  |
| regex_effbot   | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                 |
| regex_v8       | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                 |
| regex_compile  | 137 ms                                                                | 162 ms: 1.18x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                                  |
| tomli_loads          | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                                |
| xml_etree_iterparse  | 150 ms                                                                | 153 ms: 1.02x slower                                                  |
| json_loads           | 30.7 us                                                               | 31.3 us: 1.02x slower                                                 |
| unpickle_pure_python | 260 us                                                                | 267 us: 1.03x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 81.2 ms: 1.03x slower                                                 |
| pickle_pure_python   | 365 us                                                                | 392 us: 1.07x slower                                                  |
| json_dumps           | 12.3 ms                                                               | 14.3 ms: 1.17x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.72 ms: 1.04x slower                                                 |
| python_startup         | 11.4 ms                                                               | 14.5 ms: 1.28x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.15x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                 |
| genshi_text     | 27.4 ms                                                               | 32.6 ms: 1.19x slower                                                 |
| django_template | 40.7 ms                                                               | 50.6 ms: 1.25x slower                                                 |
| genshi_xml      | 60.6 ms                                                               | 78.6 ms: 1.30x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.18x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 539 ms: 1.37x faster                                                  |
| async_tree_none            | 624 ms                                                                | 473 ms: 1.32x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 448 ms: 1.29x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 604 ms: 1.29x faster                                                  |
| deepcopy_memo              | 49.6 us                                                               | 38.9 us: 1.28x faster                                                 |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 764 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 744 ms: 1.19x faster                                                  |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                                |
| deepcopy                   | 446 us                                                                | 379 us: 1.17x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 21.8 ms: 1.12x faster                                                 |
| async_tree_io_tg           | 1.40 sec                                                              | 1.26 sec: 1.11x faster                                                |
| deepcopy_reduce            | 4.10 us                                                               | 3.87 us: 1.06x faster                                                 |
| logging_format             | 8.34 us                                                               | 7.99 us: 1.04x faster                                                 |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                                  |
| logging_simple             | 7.63 us                                                               | 7.38 us: 1.03x faster                                                 |
| comprehensions             | 25.4 us                                                               | 24.6 us: 1.03x faster                                                 |
| coroutines                 | 29.0 ms                                                               | 28.7 ms: 1.01x faster                                                 |
| regex_dna                  | 254 ms                                                                | 252 ms: 1.01x faster                                                  |
| raytrace                   | 353 ms                                                                | 351 ms: 1.01x faster                                                  |
| thrift                     | 937 us                                                                | 941 us: 1.00x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                                |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                  |
| mdp                        | 3.41 sec                                                              | 3.47 sec: 1.02x slower                                                |
| xml_etree_iterparse        | 150 ms                                                                | 153 ms: 1.02x slower                                                  |
| json                       | 5.54 ms                                                               | 5.64 ms: 1.02x slower                                                 |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                 |
| scimark_sor                | 150 ms                                                                | 153 ms: 1.02x slower                                                  |
| json_loads                 | 30.7 us                                                               | 31.3 us: 1.02x slower                                                 |
| unpickle_pure_python       | 260 us                                                                | 267 us: 1.03x slower                                                  |
| xml_etree_process          | 79.0 ms                                                               | 81.2 ms: 1.03x slower                                                 |
| async_generators           | 491 ms                                                                | 506 ms: 1.03x slower                                                  |
| bench_thread_pool          | 1.31 ms                                                               | 1.36 ms: 1.04x slower                                                 |
| python_startup_no_site     | 8.37 ms                                                               | 8.72 ms: 1.04x slower                                                 |
| crypto_pyaes               | 86.6 ms                                                               | 90.5 ms: 1.04x slower                                                 |
| scimark_lu                 | 146 ms                                                                | 152 ms: 1.05x slower                                                  |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                  |
| float                      | 92.1 ms                                                               | 97.0 ms: 1.05x slower                                                 |
| tornado_http               | 136 ms                                                                | 143 ms: 1.06x slower                                                  |
| scimark_monte_carlo        | 85.1 ms                                                               | 90.0 ms: 1.06x slower                                                 |
| regex_effbot               | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                 |
| pickle_pure_python         | 365 us                                                                | 392 us: 1.07x slower                                                  |
| scimark_fft                | 418 ms                                                                | 454 ms: 1.08x slower                                                  |
| deltablue                  | 4.12 ms                                                               | 4.49 ms: 1.09x slower                                                 |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                  |
| richards_super             | 58.5 ms                                                               | 63.9 ms: 1.09x slower                                                 |
| regex_v8                   | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                 |
| html5lib                   | 65.1 ms                                                               | 71.7 ms: 1.10x slower                                                 |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.11x slower                                                  |
| telco                      | 8.51 ms                                                               | 9.49 ms: 1.12x slower                                                 |
| go                         | 157 ms                                                                | 177 ms: 1.13x slower                                                  |
| pyflate                    | 559 ms                                                                | 636 ms: 1.14x slower                                                  |
| coverage                   | 87.3 ms                                                               | 99.9 ms: 1.14x slower                                                 |
| sqlglot_parse              | 1.46 ms                                                               | 1.68 ms: 1.15x slower                                                 |
| fannkuch                   | 443 ms                                                                | 513 ms: 1.16x slower                                                  |
| typing_runtime_protocols   | 181 us                                                                | 210 us: 1.16x slower                                                  |
| docutils                   | 2.98 sec                                                              | 3.48 sec: 1.17x slower                                                |
| json_dumps                 | 12.3 ms                                                               | 14.3 ms: 1.17x slower                                                 |
| richards                   | 50.9 ms                                                               | 59.7 ms: 1.17x slower                                                 |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.27 ms: 1.17x slower                                                 |
| pycparser                  | 1.26 sec                                                              | 1.48 sec: 1.18x slower                                                |
| sqlglot_transpile          | 1.83 ms                                                               | 2.15 ms: 1.18x slower                                                 |
| 2to3                       | 308 ms                                                                | 363 ms: 1.18x slower                                                  |
| regex_compile              | 137 ms                                                                | 162 ms: 1.18x slower                                                  |
| genshi_text                | 27.4 ms                                                               | 32.6 ms: 1.19x slower                                                 |
| sqlglot_normalize          | 126 ms                                                                | 150 ms: 1.19x slower                                                  |
| chaos                      | 71.4 ms                                                               | 85.4 ms: 1.20x slower                                                 |
| spectral_norm              | 131 ms                                                                | 159 ms: 1.21x slower                                                  |
| dulwich_log                | 62.0 ms                                                               | 75.8 ms: 1.22x slower                                                 |
| sympy_str                  | 280 ms                                                                | 343 ms: 1.23x slower                                                  |
| sympy_expand               | 454 ms                                                                | 563 ms: 1.24x slower                                                  |
| pylint                     | 355 ms                                                                | 442 ms: 1.25x slower                                                  |
| django_template            | 40.7 ms                                                               | 50.6 ms: 1.25x slower                                                 |
| sqlglot_optimize           | 61.3 ms                                                               | 77.0 ms: 1.26x slower                                                 |
| nqueens                    | 99.2 ms                                                               | 126 ms: 1.27x slower                                                  |
| python_startup             | 11.4 ms                                                               | 14.5 ms: 1.28x slower                                                 |
| genshi_xml                 | 60.6 ms                                                               | 78.6 ms: 1.30x slower                                                 |
| sympy_sum                  | 154 ms                                                                | 205 ms: 1.33x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.22 sec: 1.34x slower                                                |
| sympy_integrate            | 21.6 ms                                                               | 28.9 ms: 1.34x slower                                                 |
| generators                 | 43.5 ms                                                               | 58.8 ms: 1.35x slower                                                 |
| pprint_pformat             | 1.88 sec                                                              | 2.58 sec: 1.37x slower                                                |
| hexiom                     | 6.98 ms                                                               | 9.81 ms: 1.41x slower                                                 |
| gc_traversal               | 4.40 ms                                                               | 6.29 ms: 1.43x slower                                                 |
| create_gc_cycles           | 1.92 ms                                                               | 3.64 ms: 1.90x slower                                                 |
| bench_mp_pool              | 7.05 ms                                                               | 4.29 sec: 608.14x slower                                              |
| Geometric mean             | (ref)                                                                 | 1.16x slower                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, xml_etree_generate
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (2) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: bpe_tokeniser, sphinx

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.12x