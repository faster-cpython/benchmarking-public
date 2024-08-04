# Results vs. 3.12.0

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-aarch64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.05x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 365 ms: 1.18x slower                                                       |
| docutils       | 2.98 sec                                                              | 3.67 sec: 1.23x slower                                                     |
| html5lib       | 65.1 ms                                                               | 70.5 ms: 1.08x slower                                                      |
| tornado_http   | 136 ms                                                                | 138 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 433 ms: 1.44x faster                                                       |
| async_tree_none_tg         | 577 ms                                                                | 410 ms: 1.41x faster                                                       |
| async_tree_memoization_tg  | 740 ms                                                                | 541 ms: 1.37x faster                                                       |
| async_tree_memoization     | 777 ms                                                                | 576 ms: 1.35x faster                                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 1.10 sec: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 700 ms: 1.26x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.24x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 745 ms: 1.22x faster                                                       |
| Geometric mean             | (ref)                                                                 | 1.32x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 91.2 ms: 1.01x faster                                                      |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                       |
| nbody          | 105 ms                                                                | 113 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 248 ms: 1.02x faster                                                       |
| regex_effbot   | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                                      |
| regex_v8       | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                                      |
| regex_compile  | 137 ms                                                                | 181 ms: 1.32x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 150 ms                                                                | 146 ms: 1.03x faster                                                       |
| xml_etree_process    | 79.0 ms                                                               | 79.8 ms: 1.01x slower                                                      |
| tomli_loads          | 2.59 sec                                                              | 2.66 sec: 1.02x slower                                                     |
| json_loads           | 30.7 us                                                               | 32.6 us: 1.06x slower                                                      |
| xml_etree_generate   | 112 ms                                                                | 119 ms: 1.06x slower                                                       |
| unpickle_pure_python | 260 us                                                                | 278 us: 1.07x slower                                                       |
| pickle_pure_python   | 365 us                                                                | 399 us: 1.09x slower                                                       |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.86 ms: 1.06x slower                                                      |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 12.9 ms: 1.00x faster                                                      |
| django_template | 40.7 ms                                                               | 50.6 ms: 1.24x slower                                                      |
| genshi_text     | 27.4 ms                                                               | 36.5 ms: 1.33x slower                                                      |
| genshi_xml      | 60.6 ms                                                               | 82.9 ms: 1.37x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.23x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 433 ms: 1.44x faster                                                       |
| async_tree_none_tg         | 577 ms                                                                | 410 ms: 1.41x faster                                                       |
| async_tree_memoization_tg  | 740 ms                                                                | 541 ms: 1.37x faster                                                       |
| async_tree_memoization     | 777 ms                                                                | 576 ms: 1.35x faster                                                       |
| deepcopy_memo              | 49.6 us                                                               | 38.7 us: 1.28x faster                                                      |
| async_tree_io_tg           | 1.40 sec                                                              | 1.10 sec: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 700 ms: 1.26x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.24x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 745 ms: 1.22x faster                                                       |
| deepcopy                   | 446 us                                                                | 381 us: 1.17x faster                                                       |
| generators                 | 43.5 ms                                                               | 37.5 ms: 1.16x faster                                                      |
| pathlib                    | 24.5 ms                                                               | 22.0 ms: 1.12x faster                                                      |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                       |
| comprehensions             | 25.4 us                                                               | 23.7 us: 1.07x faster                                                      |
| logging_format             | 8.34 us                                                               | 7.92 us: 1.05x faster                                                      |
| logging_simple             | 7.63 us                                                               | 7.32 us: 1.04x faster                                                      |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 150 ms                                                                | 146 ms: 1.03x faster                                                       |
| regex_dna                  | 254 ms                                                                | 248 ms: 1.02x faster                                                       |
| coroutines                 | 29.0 ms                                                               | 28.4 ms: 1.02x faster                                                      |
| float                      | 92.1 ms                                                               | 91.2 ms: 1.01x faster                                                      |
| mako                       | 12.9 ms                                                               | 12.9 ms: 1.00x faster                                                      |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                       |
| xml_etree_process          | 79.0 ms                                                               | 79.8 ms: 1.01x slower                                                      |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.01x slower                                                      |
| tornado_http               | 136 ms                                                                | 138 ms: 1.02x slower                                                       |
| mdp                        | 3.41 sec                                                              | 3.49 sec: 1.02x slower                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.66 sec: 1.02x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.25 sec: 1.03x slower                                                     |
| async_generators           | 491 ms                                                                | 505 ms: 1.03x slower                                                       |
| dask                       | 376 ms                                                                | 392 ms: 1.04x slower                                                       |
| meteor_contest             | 112 ms                                                                | 117 ms: 1.05x slower                                                       |
| json                       | 5.54 ms                                                               | 5.81 ms: 1.05x slower                                                      |
| thrift                     | 937 us                                                                | 983 us: 1.05x slower                                                       |
| deepcopy_reduce            | 4.10 us                                                               | 4.32 us: 1.05x slower                                                      |
| fannkuch                   | 443 ms                                                                | 469 ms: 1.06x slower                                                       |
| python_startup_no_site     | 8.37 ms                                                               | 8.86 ms: 1.06x slower                                                      |
| regex_effbot               | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                                      |
| json_loads                 | 30.7 us                                                               | 32.6 us: 1.06x slower                                                      |
| richards_super             | 58.5 ms                                                               | 62.2 ms: 1.06x slower                                                      |
| xml_etree_generate         | 112 ms                                                                | 119 ms: 1.06x slower                                                       |
| scimark_monte_carlo        | 85.1 ms                                                               | 90.6 ms: 1.07x slower                                                      |
| unpickle_pure_python       | 260 us                                                                | 278 us: 1.07x slower                                                       |
| logging_silent             | 127 ns                                                                | 136 ns: 1.08x slower                                                       |
| nbody                      | 105 ms                                                                | 113 ms: 1.08x slower                                                       |
| deltablue                  | 4.12 ms                                                               | 4.46 ms: 1.08x slower                                                      |
| html5lib                   | 65.1 ms                                                               | 70.5 ms: 1.08x slower                                                      |
| richards                   | 50.9 ms                                                               | 55.2 ms: 1.08x slower                                                      |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.73 ms: 1.09x slower                                                      |
| spectral_norm              | 131 ms                                                                | 143 ms: 1.09x slower                                                       |
| scimark_fft                | 418 ms                                                                | 458 ms: 1.09x slower                                                       |
| pickle_pure_python         | 365 us                                                                | 399 us: 1.09x slower                                                       |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.10x slower                                                      |
| regex_v8                   | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                                      |
| sqlglot_parse              | 1.46 ms                                                               | 1.62 ms: 1.10x slower                                                      |
| asyncio_tcp                | 566 ms                                                                | 626 ms: 1.11x slower                                                       |
| sqlglot_transpile          | 1.83 ms                                                               | 2.04 ms: 1.12x slower                                                      |
| gc_traversal               | 4.40 ms                                                               | 4.91 ms: 1.12x slower                                                      |
| pycparser                  | 1.26 sec                                                              | 1.41 sec: 1.13x slower                                                     |
| pyflate                    | 559 ms                                                                | 631 ms: 1.13x slower                                                       |
| coverage                   | 87.3 ms                                                               | 98.7 ms: 1.13x slower                                                      |
| bench_mp_pool              | 7.05 ms                                                               | 7.98 ms: 1.13x slower                                                      |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                      |
| go                         | 157 ms                                                                | 180 ms: 1.15x slower                                                       |
| sqlglot_normalize          | 126 ms                                                                | 147 ms: 1.17x slower                                                       |
| typing_runtime_protocols   | 181 us                                                                | 211 us: 1.17x slower                                                       |
| sqlglot_optimize           | 61.3 ms                                                               | 71.9 ms: 1.17x slower                                                      |
| 2to3                       | 308 ms                                                                | 365 ms: 1.18x slower                                                       |
| scimark_sor                | 150 ms                                                                | 177 ms: 1.19x slower                                                       |
| nqueens                    | 99.2 ms                                                               | 119 ms: 1.20x slower                                                       |
| pylint                     | 355 ms                                                                | 430 ms: 1.21x slower                                                       |
| sympy_str                  | 280 ms                                                                | 341 ms: 1.22x slower                                                       |
| create_gc_cycles           | 1.92 ms                                                               | 2.34 ms: 1.22x slower                                                      |
| pprint_safe_repr           | 916 ms                                                                | 1.12 sec: 1.22x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.67 sec: 1.23x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 2.33 sec: 1.24x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 26.8 ms: 1.24x slower                                                      |
| django_template            | 40.7 ms                                                               | 50.6 ms: 1.24x slower                                                      |
| telco                      | 8.51 ms                                                               | 10.6 ms: 1.25x slower                                                      |
| chaos                      | 71.4 ms                                                               | 89.1 ms: 1.25x slower                                                      |
| scimark_lu                 | 146 ms                                                                | 184 ms: 1.27x slower                                                       |
| sympy_sum                  | 154 ms                                                                | 197 ms: 1.28x slower                                                       |
| sympy_expand               | 454 ms                                                                | 580 ms: 1.28x slower                                                       |
| hexiom                     | 6.98 ms                                                               | 9.11 ms: 1.31x slower                                                      |
| regex_compile              | 137 ms                                                                | 181 ms: 1.32x slower                                                       |
| genshi_text                | 27.4 ms                                                               | 36.5 ms: 1.33x slower                                                      |
| genshi_xml                 | 60.6 ms                                                               | 82.9 ms: 1.37x slower                                                      |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                               |

Benchmark hidden because not significant (2): asyncio_websockets, crypto_pyaes
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240727-3.14.0a0-60b7e71-JIT/bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json: bpe_tokeniser

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x