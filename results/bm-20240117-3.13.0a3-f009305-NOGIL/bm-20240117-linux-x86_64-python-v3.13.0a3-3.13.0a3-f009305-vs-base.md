# Results vs. base

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-NOGIL/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| 2to3           | 270 ms                                                                                               | 290 ms: 1.07x slower                                                                                       |
| chameleon      | 6.87 ms                                                                                              | 7.87 ms: 1.15x slower                                                                                      |
| docutils       | 2.68 sec                                                                                             | 2.95 sec: 1.10x slower                                                                                     |
| html5lib       | 67.9 ms                                                                                              | 70.5 ms: 1.04x slower                                                                                      |
| tornado_http   | 96.8 ms                                                                                              | 102 ms: 1.05x slower                                                                                       |
| Geometric mean | (ref)                                                                                                | 1.08x slower                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-NOGIL/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 734 ms                                                                                               | 848 ms: 1.16x slower                                                                                       |
| async_tree_cpu_io_mixed    | 724 ms                                                                                               | 838 ms: 1.16x slower                                                                                       |
| async_tree_none            | 446 ms                                                                                               | 533 ms: 1.20x slower                                                                                       |
| async_tree_memoization_tg  | 586 ms                                                                                               | 702 ms: 1.20x slower                                                                                       |
| async_tree_none_tg         | 447 ms                                                                                               | 537 ms: 1.20x slower                                                                                       |
| async_tree_memoization     | 574 ms                                                                                               | 704 ms: 1.23x slower                                                                                       |
| async_tree_io              | 1.21 sec                                                                                             | 1.49 sec: 1.23x slower                                                                                     |
| async_tree_io_tg           | 1.21 sec                                                                                             | 1.50 sec: 1.23x slower                                                                                     |
| Geometric mean             | (ref)                                                                                                | 1.20x slower                                                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-NOGIL/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                                                               | 186 ms: 1.02x faster                                                                                       |
| float          | 82.0 ms                                                                                              | 88.3 ms: 1.08x slower                                                                                      |
| nbody          | 89.5 ms                                                                                              | 105 ms: 1.18x slower                                                                                       |
| Geometric mean | (ref)                                                                                                | 1.07x slower                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-NOGIL/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| regex_v8       | 25.4 ms                                                                                              | 23.7 ms: 1.07x faster                                                                                      |
| regex_dna      | 230 ms                                                                                               | 218 ms: 1.05x faster                                                                                       |
| regex_effbot   | 3.68 ms                                                                                              | 3.52 ms: 1.05x faster                                                                                      |
| regex_compile  | 131 ms                                                                                               | 139 ms: 1.06x slower                                                                                       |
| Geometric mean | (ref)                                                                                                | 1.03x faster                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-NOGIL/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| pickle               | 11.5 us                                                                                              | 10.6 us: 1.09x faster                                                                                      |
| unpickle_list        | 5.25 us                                                                                              | 4.99 us: 1.05x faster                                                                                      |
| pickle_list          | 4.98 us                                                                                              | 4.87 us: 1.02x faster                                                                                      |
| pickle_dict          | 33.8 us                                                                                              | 33.2 us: 1.02x faster                                                                                      |
| json_loads           | 28.7 us                                                                                              | 29.3 us: 1.02x slower                                                                                      |
| tomli_loads          | 2.16 sec                                                                                             | 2.24 sec: 1.04x slower                                                                                     |
| json_dumps           | 10.5 ms                                                                                              | 11.0 ms: 1.05x slower                                                                                      |
| pickle_pure_python   | 302 us                                                                                               | 318 us: 1.05x slower                                                                                       |
| xml_etree_iterparse  | 106 ms                                                                                               | 114 ms: 1.07x slower                                                                                       |
| xml_etree_parse      | 161 ms                                                                                               | 172 ms: 1.07x slower                                                                                       |
| unpickle_pure_python | 218 us                                                                                               | 234 us: 1.07x slower                                                                                       |
| xml_etree_generate   | 87.4 ms                                                                                              | 94.2 ms: 1.08x slower                                                                                      |
| xml_etree_process    | 59.9 ms                                                                                              | 65.4 ms: 1.09x slower                                                                                      |
| Geometric mean       | (ref)                                                                                                | 1.02x slower                                                                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-NOGIL/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| python_startup         | 10.4 ms                                                                                              | 12.1 ms: 1.17x slower                                                                                      |
| python_startup_no_site | 8.92 ms                                                                                              | 10.5 ms: 1.17x slower                                                                                      |
| Geometric mean         | (ref)                                                                                                | 1.17x slower                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-NOGIL/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|-----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                                                              | 55.0 ms: 1.06x slower                                                                                      |
| genshi_text     | 23.2 ms                                                                                              | 24.6 ms: 1.06x slower                                                                                      |
| mako            | 11.3 ms                                                                                              | 12.0 ms: 1.07x slower                                                                                      |
| django_template | 34.7 ms                                                                                              | 37.3 ms: 1.07x slower                                                                                      |
| Geometric mean  | (ref)                                                                                                | 1.06x slower                                                                                               |

All benchmarks:
===============

| Benchmark                  | results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json | results/bm-20240117-3.13.0a3-f009305-NOGIL/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json |
|----------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| create_gc_cycles           | 1.51 ms                                                                                              | 1.26 ms: 1.20x faster                                                                                      |
| pickle                     | 11.5 us                                                                                              | 10.6 us: 1.09x faster                                                                                      |
| gc_traversal               | 3.78 ms                                                                                              | 3.52 ms: 1.08x faster                                                                                      |
| regex_v8                   | 25.4 ms                                                                                              | 23.7 ms: 1.07x faster                                                                                      |
| regex_dna                  | 230 ms                                                                                               | 218 ms: 1.05x faster                                                                                       |
| unpickle_list              | 5.25 us                                                                                              | 4.99 us: 1.05x faster                                                                                      |
| regex_effbot               | 3.68 ms                                                                                              | 3.52 ms: 1.05x faster                                                                                      |
| pidigits                   | 191 ms                                                                                               | 186 ms: 1.02x faster                                                                                       |
| pickle_list                | 4.98 us                                                                                              | 4.87 us: 1.02x faster                                                                                      |
| pickle_dict                | 33.8 us                                                                                              | 33.2 us: 1.02x faster                                                                                      |
| bench_mp_pool              | 23.8 ms                                                                                              | 23.5 ms: 1.01x faster                                                                                      |
| pyflate                    | 471 ms                                                                                               | 469 ms: 1.01x faster                                                                                       |
| asyncio_websockets         | 563 ms                                                                                               | 560 ms: 1.01x faster                                                                                       |
| richards                   | 48.9 ms                                                                                              | 49.6 ms: 1.01x slower                                                                                      |
| richards_super             | 55.1 ms                                                                                              | 56.0 ms: 1.02x slower                                                                                      |
| spectral_norm              | 111 ms                                                                                               | 113 ms: 1.02x slower                                                                                       |
| json_loads                 | 28.7 us                                                                                              | 29.3 us: 1.02x slower                                                                                      |
| scimark_sor                | 131 ms                                                                                               | 134 ms: 1.02x slower                                                                                       |
| pathlib                    | 18.5 ms                                                                                              | 18.9 ms: 1.02x slower                                                                                      |
| dulwich_log                | 66.8 ms                                                                                              | 68.4 ms: 1.02x slower                                                                                      |
| crypto_pyaes               | 72.3 ms                                                                                              | 74.5 ms: 1.03x slower                                                                                      |
| sqlglot_normalize          | 109 ms                                                                                               | 113 ms: 1.03x slower                                                                                       |
| asyncio_tcp                | 493 ms                                                                                               | 510 ms: 1.03x slower                                                                                       |
| html5lib                   | 67.9 ms                                                                                              | 70.5 ms: 1.04x slower                                                                                      |
| tomli_loads                | 2.16 sec                                                                                             | 2.24 sec: 1.04x slower                                                                                     |
| asyncio_tcp_ssl            | 1.83 sec                                                                                             | 1.90 sec: 1.04x slower                                                                                     |
| sqlglot_optimize           | 54.8 ms                                                                                              | 57.3 ms: 1.05x slower                                                                                      |
| deepcopy                   | 350 us                                                                                               | 368 us: 1.05x slower                                                                                       |
| async_generators           | 454 ms                                                                                               | 476 ms: 1.05x slower                                                                                       |
| gunicorn                   | 1.27 ms                                                                                              | 1.33 ms: 1.05x slower                                                                                      |
| json_dumps                 | 10.5 ms                                                                                              | 11.0 ms: 1.05x slower                                                                                      |
| meteor_contest             | 110 ms                                                                                               | 115 ms: 1.05x slower                                                                                       |
| pickle_pure_python         | 302 us                                                                                               | 318 us: 1.05x slower                                                                                       |
| deepcopy_reduce            | 3.11 us                                                                                              | 3.27 us: 1.05x slower                                                                                      |
| tornado_http               | 96.8 ms                                                                                              | 102 ms: 1.05x slower                                                                                       |
| aiohttp                    | 1.17 ms                                                                                              | 1.23 ms: 1.05x slower                                                                                      |
| genshi_xml                 | 52.1 ms                                                                                              | 55.0 ms: 1.06x slower                                                                                      |
| nqueens                    | 80.7 ms                                                                                              | 85.2 ms: 1.06x slower                                                                                      |
| scimark_lu                 | 114 ms                                                                                               | 120 ms: 1.06x slower                                                                                       |
| logging_silent             | 105 ns                                                                                               | 111 ns: 1.06x slower                                                                                       |
| coroutines                 | 22.3 ms                                                                                              | 23.6 ms: 1.06x slower                                                                                      |
| scimark_sparse_mat_mult    | 5.10 ms                                                                                              | 5.42 ms: 1.06x slower                                                                                      |
| regex_compile              | 131 ms                                                                                               | 139 ms: 1.06x slower                                                                                       |
| sqlglot_transpile          | 1.61 ms                                                                                              | 1.71 ms: 1.06x slower                                                                                      |
| genshi_text                | 23.2 ms                                                                                              | 24.6 ms: 1.06x slower                                                                                      |
| logging_simple             | 5.89 us                                                                                              | 6.26 us: 1.06x slower                                                                                      |
| telco                      | 8.55 ms                                                                                              | 9.10 ms: 1.06x slower                                                                                      |
| mako                       | 11.3 ms                                                                                              | 12.0 ms: 1.07x slower                                                                                      |
| pprint_pformat             | 1.53 sec                                                                                             | 1.64 sec: 1.07x slower                                                                                     |
| logging_format             | 6.53 us                                                                                              | 6.96 us: 1.07x slower                                                                                      |
| sqlglot_parse              | 1.28 ms                                                                                              | 1.36 ms: 1.07x slower                                                                                      |
| pprint_safe_repr           | 745 ms                                                                                               | 796 ms: 1.07x slower                                                                                       |
| go                         | 140 ms                                                                                               | 149 ms: 1.07x slower                                                                                       |
| xml_etree_iterparse        | 106 ms                                                                                               | 114 ms: 1.07x slower                                                                                       |
| scimark_fft                | 366 ms                                                                                               | 391 ms: 1.07x slower                                                                                       |
| xml_etree_parse            | 161 ms                                                                                               | 172 ms: 1.07x slower                                                                                       |
| pylint                     | 313 ms                                                                                               | 335 ms: 1.07x slower                                                                                       |
| unpickle_pure_python       | 218 us                                                                                               | 234 us: 1.07x slower                                                                                       |
| 2to3                       | 270 ms                                                                                               | 290 ms: 1.07x slower                                                                                       |
| django_template            | 34.7 ms                                                                                              | 37.3 ms: 1.07x slower                                                                                      |
| float                      | 82.0 ms                                                                                              | 88.3 ms: 1.08x slower                                                                                      |
| xml_etree_generate         | 87.4 ms                                                                                              | 94.2 ms: 1.08x slower                                                                                      |
| scimark_monte_carlo        | 68.6 ms                                                                                              | 74.0 ms: 1.08x slower                                                                                      |
| pycparser                  | 1.19 sec                                                                                             | 1.29 sec: 1.08x slower                                                                                     |
| comprehensions             | 16.3 us                                                                                              | 17.7 us: 1.09x slower                                                                                      |
| hexiom                     | 6.10 ms                                                                                              | 6.64 ms: 1.09x slower                                                                                      |
| chaos                      | 59.9 ms                                                                                              | 65.2 ms: 1.09x slower                                                                                      |
| sqlite_synth               | 2.88 us                                                                                              | 3.15 us: 1.09x slower                                                                                      |
| xml_etree_process          | 59.9 ms                                                                                              | 65.4 ms: 1.09x slower                                                                                      |
| deltablue                  | 3.23 ms                                                                                              | 3.56 ms: 1.10x slower                                                                                      |
| docutils                   | 2.68 sec                                                                                             | 2.95 sec: 1.10x slower                                                                                     |
| raytrace                   | 264 ms                                                                                               | 291 ms: 1.10x slower                                                                                       |
| deepcopy_memo              | 38.4 us                                                                                              | 42.4 us: 1.10x slower                                                                                      |
| generators                 | 29.2 ms                                                                                              | 32.3 ms: 1.11x slower                                                                                      |
| typing_runtime_protocols   | 110 us                                                                                               | 124 us: 1.12x slower                                                                                       |
| mdp                        | 2.58 sec                                                                                             | 2.93 sec: 1.13x slower                                                                                     |
| chameleon                  | 6.87 ms                                                                                              | 7.87 ms: 1.15x slower                                                                                      |
| sympy_integrate            | 20.0 ms                                                                                              | 23.0 ms: 1.15x slower                                                                                      |
| async_tree_cpu_io_mixed_tg | 734 ms                                                                                               | 848 ms: 1.16x slower                                                                                       |
| async_tree_cpu_io_mixed    | 724 ms                                                                                               | 838 ms: 1.16x slower                                                                                       |
| python_startup             | 10.4 ms                                                                                              | 12.1 ms: 1.17x slower                                                                                      |
| python_startup_no_site     | 8.92 ms                                                                                              | 10.5 ms: 1.17x slower                                                                                      |
| nbody                      | 89.5 ms                                                                                              | 105 ms: 1.18x slower                                                                                       |
| async_tree_none            | 446 ms                                                                                               | 533 ms: 1.20x slower                                                                                       |
| async_tree_memoization_tg  | 586 ms                                                                                               | 702 ms: 1.20x slower                                                                                       |
| async_tree_none_tg         | 447 ms                                                                                               | 537 ms: 1.20x slower                                                                                       |
| async_tree_memoization     | 574 ms                                                                                               | 704 ms: 1.23x slower                                                                                       |
| async_tree_io              | 1.21 sec                                                                                             | 1.49 sec: 1.23x slower                                                                                     |
| async_tree_io_tg           | 1.21 sec                                                                                             | 1.50 sec: 1.23x slower                                                                                     |
| sympy_str                  | 275 ms                                                                                               | 342 ms: 1.25x slower                                                                                       |
| mypy2                      | 865 ms                                                                                               | 1.18 sec: 1.37x slower                                                                                     |
| sympy_expand               | 466 ms                                                                                               | 644 ms: 1.38x slower                                                                                       |
| sympy_sum                  | 152 ms                                                                                               | 216 ms: 1.42x slower                                                                                       |
| flaskblogging              | 8.79 ms                                                                                              | 12.6 ms: 1.44x slower                                                                                      |
| bench_thread_pool          | 842 us                                                                                               | 2.54 ms: 3.01x slower                                                                                      |
| coverage                   | 95.8 ms                                                                                              | 690 ms: 7.20x slower                                                                                       |
| thrift                     | 796 us                                                                                               | 9.30 ms: 11.68x slower                                                                                     |
| fannkuch                   | 402 ms                                                                                               | 4.97 sec: 12.35x slower                                                                                    |
| Geometric mean             | (ref)                                                                                                | 1.16x slower                                                                                               |

Benchmark hidden because not significant (2): json, unpickle
Ignored benchmarks (1) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: djangocms

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.13x