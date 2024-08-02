# Results vs. 3.12.0

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: linux-aarch64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.01x faster
- HPT reliability: 50.42%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 303 ms: 1.02x faster                                                         |
| chameleon      | 8.81 ms                                                               | 9.33 ms: 1.06x slower                                                        |
| docutils       | 2.98 sec                                                              | 3.11 sec: 1.04x slower                                                       |
| html5lib       | 65.1 ms                                                               | 65.9 ms: 1.01x slower                                                        |
| tornado_http   | 136 ms                                                                | 129 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 489 ms: 1.28x faster                                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 589 ms: 1.26x faster                                                         |
| async_tree_none_tg         | 577 ms                                                                | 465 ms: 1.24x faster                                                         |
| async_tree_memoization     | 777 ms                                                                | 644 ms: 1.21x faster                                                         |
| async_tree_io              | 1.41 sec                                                              | 1.22 sec: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 787 ms: 1.16x faster                                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 787 ms: 1.12x faster                                                         |
| Geometric mean             | (ref)                                                                 | 1.19x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 91.5 ms: 1.01x faster                                                        |
| pidigits       | 233 ms                                                                | 234 ms: 1.00x slower                                                         |
| nbody          | 105 ms                                                                | 111 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 129 ms: 1.06x faster                                                         |
| regex_dna      | 254 ms                                                                | 246 ms: 1.03x faster                                                         |
| regex_effbot   | 4.64 ms                                                               | 4.85 ms: 1.05x slower                                                        |
| regex_v8       | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 365 us                                                                | 355 us: 1.03x faster                                                         |
| unpickle_pure_python | 260 us                                                                | 254 us: 1.02x faster                                                         |
| xml_etree_parse      | 195 ms                                                                | 191 ms: 1.02x faster                                                         |
| pickle               | 13.4 us                                                               | 13.5 us: 1.01x slower                                                        |
| xml_etree_generate   | 112 ms                                                                | 113 ms: 1.01x slower                                                         |
| pickle_dict          | 37.3 us                                                               | 37.7 us: 1.01x slower                                                        |
| xml_etree_process    | 79.0 ms                                                               | 79.8 ms: 1.01x slower                                                        |
| tomli_loads          | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                       |
| pickle_list          | 5.25 us                                                               | 5.31 us: 1.01x slower                                                        |
| json_loads           | 30.7 us                                                               | 32.6 us: 1.06x slower                                                        |
| unpickle             | 18.5 us                                                               | 19.8 us: 1.07x slower                                                        |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                        |
| unpickle_list        | 6.17 us                                                               | 6.67 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.42 ms: 1.01x slower                                                        |
| python_startup         | 11.4 ms                                                               | 12.5 ms: 1.10x slower                                                        |
| Geometric mean         | (ref)                                                                 | 1.05x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.7 ms: 1.01x slower                                                        |
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                        |
| django_template | 40.7 ms                                                               | 41.9 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 489 ms: 1.28x faster                                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 589 ms: 1.26x faster                                                         |
| comprehensions             | 25.4 us                                                               | 20.3 us: 1.25x faster                                                        |
| async_tree_none_tg         | 577 ms                                                                | 465 ms: 1.24x faster                                                         |
| async_tree_memoization     | 777 ms                                                                | 644 ms: 1.21x faster                                                         |
| raytrace                   | 353 ms                                                                | 295 ms: 1.20x faster                                                         |
| async_tree_io              | 1.41 sec                                                              | 1.22 sec: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 787 ms: 1.16x faster                                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.14x faster                                                       |
| generators                 | 43.5 ms                                                               | 38.4 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 787 ms: 1.12x faster                                                         |
| chaos                      | 71.4 ms                                                               | 66.2 ms: 1.08x faster                                                        |
| deltablue                  | 4.12 ms                                                               | 3.84 ms: 1.07x faster                                                        |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.07x faster                                                         |
| regex_compile              | 137 ms                                                                | 129 ms: 1.06x faster                                                         |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                        |
| pathlib                    | 24.5 ms                                                               | 23.3 ms: 1.05x faster                                                        |
| tornado_http               | 136 ms                                                                | 129 ms: 1.05x faster                                                         |
| logging_format             | 8.34 us                                                               | 7.93 us: 1.05x faster                                                        |
| sqlglot_parse              | 1.46 ms                                                               | 1.39 ms: 1.05x faster                                                        |
| dulwich_log                | 62.0 ms                                                               | 59.2 ms: 1.05x faster                                                        |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.3 ms: 1.05x faster                                                        |
| logging_simple             | 7.63 us                                                               | 7.31 us: 1.04x faster                                                        |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.04x faster                                                         |
| sympy_str                  | 280 ms                                                                | 269 ms: 1.04x faster                                                         |
| bench_thread_pool          | 1.31 ms                                                               | 1.26 ms: 1.04x faster                                                        |
| regex_dna                  | 254 ms                                                                | 246 ms: 1.03x faster                                                         |
| mdp                        | 3.41 sec                                                              | 3.31 sec: 1.03x faster                                                       |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                       |
| pickle_pure_python         | 365 us                                                                | 355 us: 1.03x faster                                                         |
| crypto_pyaes               | 86.6 ms                                                               | 84.3 ms: 1.03x faster                                                        |
| sympy_integrate            | 21.6 ms                                                               | 21.1 ms: 1.03x faster                                                        |
| unpickle_pure_python       | 260 us                                                                | 254 us: 1.02x faster                                                         |
| xml_etree_parse            | 195 ms                                                                | 191 ms: 1.02x faster                                                         |
| 2to3                       | 308 ms                                                                | 303 ms: 1.02x faster                                                         |
| async_generators           | 491 ms                                                                | 484 ms: 1.01x faster                                                         |
| float                      | 92.1 ms                                                               | 91.5 ms: 1.01x faster                                                        |
| deepcopy_reduce            | 4.10 us                                                               | 4.08 us: 1.00x faster                                                        |
| pidigits                   | 233 ms                                                                | 234 ms: 1.00x slower                                                         |
| python_startup_no_site     | 8.37 ms                                                               | 8.42 ms: 1.01x slower                                                        |
| sympy_expand               | 454 ms                                                                | 457 ms: 1.01x slower                                                         |
| pickle                     | 13.4 us                                                               | 13.5 us: 1.01x slower                                                        |
| xml_etree_generate         | 112 ms                                                                | 113 ms: 1.01x slower                                                         |
| deepcopy                   | 446 us                                                                | 449 us: 1.01x slower                                                         |
| pickle_dict                | 37.3 us                                                               | 37.7 us: 1.01x slower                                                        |
| thrift                     | 937 us                                                                | 945 us: 1.01x slower                                                         |
| genshi_text                | 27.4 ms                                                               | 27.7 ms: 1.01x slower                                                        |
| deepcopy_memo              | 49.6 us                                                               | 50.1 us: 1.01x slower                                                        |
| xml_etree_process          | 79.0 ms                                                               | 79.8 ms: 1.01x slower                                                        |
| tomli_loads                | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                       |
| pickle_list                | 5.25 us                                                               | 5.31 us: 1.01x slower                                                        |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                         |
| html5lib                   | 65.1 ms                                                               | 65.9 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.22 sec: 1.01x slower                                                       |
| go                         | 157 ms                                                                | 159 ms: 1.01x slower                                                         |
| sqlglot_optimize           | 61.3 ms                                                               | 62.2 ms: 1.01x slower                                                        |
| sqlglot_normalize          | 126 ms                                                                | 128 ms: 1.02x slower                                                         |
| pprint_pformat             | 1.88 sec                                                              | 1.92 sec: 1.02x slower                                                       |
| hexiom                     | 6.98 ms                                                               | 7.12 ms: 1.02x slower                                                        |
| aiohttp                    | 1.16 ms                                                               | 1.18 ms: 1.02x slower                                                        |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                        |
| pprint_safe_repr           | 916 ms                                                                | 939 ms: 1.02x slower                                                         |
| coroutines                 | 29.0 ms                                                               | 29.8 ms: 1.03x slower                                                        |
| django_template            | 40.7 ms                                                               | 41.9 ms: 1.03x slower                                                        |
| sqlite_synth               | 3.77 us                                                               | 3.91 us: 1.04x slower                                                        |
| docutils                   | 2.98 sec                                                              | 3.11 sec: 1.04x slower                                                       |
| regex_effbot               | 4.64 ms                                                               | 4.85 ms: 1.05x slower                                                        |
| fannkuch                   | 443 ms                                                                | 464 ms: 1.05x slower                                                         |
| json                       | 5.54 ms                                                               | 5.83 ms: 1.05x slower                                                        |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.52 ms: 1.05x slower                                                        |
| spectral_norm              | 131 ms                                                                | 138 ms: 1.05x slower                                                         |
| nbody                      | 105 ms                                                                | 111 ms: 1.06x slower                                                         |
| scimark_fft                | 418 ms                                                                | 443 ms: 1.06x slower                                                         |
| chameleon                  | 8.81 ms                                                               | 9.33 ms: 1.06x slower                                                        |
| json_loads                 | 30.7 us                                                               | 32.6 us: 1.06x slower                                                        |
| logging_silent             | 127 ns                                                                | 135 ns: 1.06x slower                                                         |
| richards_super             | 58.5 ms                                                               | 62.2 ms: 1.06x slower                                                        |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.07x slower                                                         |
| unpickle                   | 18.5 us                                                               | 19.8 us: 1.07x slower                                                        |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                        |
| gunicorn                   | 1.14 ms                                                               | 1.22 ms: 1.08x slower                                                        |
| unpickle_list              | 6.17 us                                                               | 6.67 us: 1.08x slower                                                        |
| richards                   | 50.9 ms                                                               | 55.7 ms: 1.09x slower                                                        |
| regex_v8                   | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                                        |
| python_startup             | 11.4 ms                                                               | 12.5 ms: 1.10x slower                                                        |
| typing_runtime_protocols   | 181 us                                                                | 202 us: 1.12x slower                                                         |
| telco                      | 8.51 ms                                                               | 9.78 ms: 1.15x slower                                                        |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                         |
| gc_traversal               | 4.40 ms                                                               | 5.09 ms: 1.16x slower                                                        |
| create_gc_cycles           | 1.92 ms                                                               | 2.45 ms: 1.27x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                                 |

Benchmark hidden because not significant (9): pylint, dask, asyncio_tcp, xml_etree_iterparse, nqueens, pyflate, genshi_xml, bench_mp_pool, asyncio_websockets
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240504-3.13.0a6+-4c1049b/bm-20240504-arminc-aarch64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b.json: flaskblogging

# HPT report

- Reliability score: 50.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x