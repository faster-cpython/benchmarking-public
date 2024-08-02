# Results vs. 3.12.0

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-aarch64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 362 ms: 1.18x slower                                                     |
| chameleon      | 8.81 ms                                                               | 9.09 ms: 1.03x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.54 sec: 1.19x slower                                                   |
| html5lib       | 65.1 ms                                                               | 72.6 ms: 1.12x slower                                                    |
| tornado_http   | 136 ms                                                                | 142 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 507 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 481 ms: 1.20x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 618 ms: 1.20x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 668 ms: 1.16x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.23 sec: 1.15x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.22 sec: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 798 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 827 ms: 1.10x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 90.0 ms: 1.02x faster                                                    |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                     |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 260 ms: 1.03x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 30.2 ms: 1.06x slower                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.97 ms: 1.07x slower                                                    |
| regex_compile  | 137 ms                                                                | 178 ms: 1.29x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.04x faster                                                     |
| pickle_list          | 5.25 us                                                               | 5.30 us: 1.01x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 37.7 us: 1.01x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 113 ms: 1.01x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 80.2 ms: 1.02x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.3 us: 1.05x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.0 ms: 1.06x slower                                                    |
| unpickle             | 18.5 us                                                               | 19.7 us: 1.07x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 277 us: 1.07x slower                                                     |
| unpickle_list        | 6.17 us                                                               | 6.59 us: 1.07x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 398 us: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 11.1 ms: 1.33x slower                                                    |
| python_startup         | 11.4 ms                                                               | 15.5 ms: 1.37x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.35x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.0 ms: 1.00x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 33.9 ms: 1.23x slower                                                    |
| django_template | 40.7 ms                                                               | 50.5 ms: 1.24x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 82.6 ms: 1.36x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.20x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 507 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 481 ms: 1.20x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 618 ms: 1.20x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 668 ms: 1.16x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.23 sec: 1.15x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.22 sec: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 798 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 827 ms: 1.10x faster                                                     |
| comprehensions             | 25.4 us                                                               | 23.1 us: 1.10x faster                                                    |
| raytrace                   | 353 ms                                                                | 322 ms: 1.10x faster                                                     |
| generators                 | 43.5 ms                                                               | 39.7 ms: 1.09x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 23.2 ms: 1.06x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.98 us: 1.05x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.04x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.35 us: 1.04x faster                                                    |
| float                      | 92.1 ms                                                               | 90.0 ms: 1.02x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 49.2 us: 1.01x faster                                                    |
| mako                       | 12.9 ms                                                               | 13.0 ms: 1.00x slower                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                     |
| pickle_list                | 5.25 us                                                               | 5.30 us: 1.01x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 37.7 us: 1.01x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.45 sec: 1.01x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.81 us: 1.01x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 113 ms: 1.01x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 666 ms: 1.01x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.01x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 80.2 ms: 1.02x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 88.8 ms: 1.02x slower                                                    |
| regex_dna                  | 254 ms                                                                | 260 ms: 1.03x slower                                                     |
| json                       | 5.54 ms                                                               | 5.71 ms: 1.03x slower                                                    |
| chameleon                  | 8.81 ms                                                               | 9.09 ms: 1.03x slower                                                    |
| thrift                     | 937 us                                                                | 974 us: 1.04x slower                                                     |
| dask                       | 376 ms                                                                | 392 ms: 1.04x slower                                                     |
| fannkuch                   | 443 ms                                                                | 462 ms: 1.04x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.28 sec: 1.04x slower                                                   |
| meteor_contest             | 112 ms                                                                | 117 ms: 1.04x slower                                                     |
| tornado_http               | 136 ms                                                                | 142 ms: 1.05x slower                                                     |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 90.0 ms: 1.06x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.0 ms: 1.06x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.2 ms: 1.06x slower                                                    |
| async_generators           | 491 ms                                                                | 522 ms: 1.06x slower                                                     |
| unpickle                   | 18.5 us                                                               | 19.7 us: 1.07x slower                                                    |
| pyflate                    | 559 ms                                                                | 596 ms: 1.07x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 277 us: 1.07x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.59 us: 1.07x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.97 ms: 1.07x slower                                                    |
| richards_super             | 58.5 ms                                                               | 62.8 ms: 1.07x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.58 ms: 1.08x slower                                                    |
| mypy2                      | 873 ms                                                                | 948 ms: 1.09x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 398 us: 1.09x slower                                                     |
| richards                   | 50.9 ms                                                               | 55.7 ms: 1.09x slower                                                    |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.38 sec: 1.10x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.01 ms: 1.10x slower                                                    |
| logging_silent             | 127 ns                                                                | 139 ns: 1.10x slower                                                     |
| scimark_fft                | 418 ms                                                                | 460 ms: 1.10x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 4.55 ms: 1.10x slower                                                    |
| deepcopy                   | 446 us                                                                | 495 us: 1.11x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.89 ms: 1.11x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 630 ms: 1.11x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 72.6 ms: 1.12x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.60 us: 1.12x slower                                                    |
| spectral_norm              | 131 ms                                                                | 147 ms: 1.13x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 69.3 ms: 1.13x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 142 ms: 1.13x slower                                                     |
| aiohttp                    | 1.16 ms                                                               | 1.32 ms: 1.14x slower                                                    |
| go                         | 157 ms                                                                | 179 ms: 1.14x slower                                                     |
| coverage                   | 87.3 ms                                                               | 99.5 ms: 1.14x slower                                                    |
| sympy_str                  | 280 ms                                                                | 323 ms: 1.16x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 209 us: 1.16x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 71.8 ms: 1.16x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 8.22 ms: 1.17x slower                                                    |
| scimark_sor                | 150 ms                                                                | 175 ms: 1.17x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 117 ms: 1.17x slower                                                     |
| gc_traversal               | 4.40 ms                                                               | 5.16 ms: 1.17x slower                                                    |
| 2to3                       | 308 ms                                                                | 362 ms: 1.18x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 25.6 ms: 1.19x slower                                                    |
| pylint                     | 355 ms                                                                | 421 ms: 1.19x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.54 sec: 1.19x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.1 ms: 1.19x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 185 ms: 1.20x slower                                                     |
| gunicorn                   | 1.14 ms                                                               | 1.36 ms: 1.20x slower                                                    |
| sympy_expand               | 454 ms                                                                | 547 ms: 1.21x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.11 sec: 1.21x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.32 sec: 1.23x slower                                                   |
| chaos                      | 71.4 ms                                                               | 88.0 ms: 1.23x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 33.9 ms: 1.23x slower                                                    |
| django_template            | 40.7 ms                                                               | 50.5 ms: 1.24x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.39 ms: 1.25x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 184 ms: 1.26x slower                                                     |
| regex_compile              | 137 ms                                                                | 178 ms: 1.29x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 9.05 ms: 1.30x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 11.1 ms: 1.33x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 82.6 ms: 1.36x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.5 ms: 1.37x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_iterparse, coroutines, pickle
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.01x