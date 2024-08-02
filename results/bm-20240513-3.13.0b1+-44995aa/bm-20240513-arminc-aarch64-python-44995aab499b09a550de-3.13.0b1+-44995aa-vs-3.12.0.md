# Results vs. 3.12.0

- fork: python
- ref: 44995aab499b09a550de
- machine: linux-aarch64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.02x slower
- HPT reliability: 71.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 302 ms: 1.02x faster                                                     |
| chameleon      | 8.81 ms                                                               | 9.02 ms: 1.02x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                   |
| html5lib       | 65.1 ms                                                               | 68.4 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 491 ms: 1.27x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 472 ms: 1.22x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 643 ms: 1.21x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 626 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 791 ms: 1.15x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.22 sec: 1.15x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 794 ms: 1.11x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.18x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 90.5 ms: 1.02x faster                                                    |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                     |
| nbody          | 105 ms                                                                | 112 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.94 ms: 1.07x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 31.2 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 251 us: 1.04x faster                                                     |
| pickle_list          | 5.25 us                                                               | 5.12 us: 1.02x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                   |
| pickle_pure_python   | 365 us                                                                | 361 us: 1.01x faster                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                                     |
| pickle               | 13.4 us                                                               | 13.6 us: 1.01x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 81.0 ms: 1.03x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.46 us: 1.05x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.6 us: 1.06x slower                                                    |
| unpickle             | 18.5 us                                                               | 19.7 us: 1.07x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, pickle_dict, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.47 ms: 1.01x slower                                                    |
| python_startup         | 11.4 ms                                                               | 12.6 ms: 1.11x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.06x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 41.3 ms: 1.01x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 27.9 ms: 1.02x slower                                                    |
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 491 ms: 1.27x faster                                                     |
| comprehensions             | 25.4 us                                                               | 20.2 us: 1.26x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 472 ms: 1.22x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 643 ms: 1.21x faster                                                     |
| raytrace                   | 353 ms                                                                | 297 ms: 1.19x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 626 ms: 1.18x faster                                                     |
| generators                 | 43.5 ms                                                               | 37.6 ms: 1.16x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 791 ms: 1.15x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.22 sec: 1.15x faster                                                   |
| mypy2                      | 873 ms                                                                | 762 ms: 1.15x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 794 ms: 1.11x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.12 us: 1.07x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.9 ms: 1.07x faster                                                    |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 81.2 ms: 1.07x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.06x faster                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 1.72 ms: 1.06x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.88 ms: 1.06x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.88 us: 1.06x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 138 ms: 1.06x faster                                                     |
| dulwich_log                | 62.0 ms                                                               | 58.7 ms: 1.06x faster                                                    |
| chaos                      | 71.4 ms                                                               | 67.9 ms: 1.05x faster                                                    |
| sympy_str                  | 280 ms                                                                | 270 ms: 1.04x faster                                                     |
| unpickle_pure_python       | 260 us                                                                | 251 us: 1.04x faster                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.3 ms: 1.03x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.27 ms: 1.03x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                                    |
| pickle_list                | 5.25 us                                                               | 5.12 us: 1.02x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.35 sec: 1.02x faster                                                   |
| 2to3                       | 308 ms                                                                | 302 ms: 1.02x faster                                                     |
| float                      | 92.1 ms                                                               | 90.5 ms: 1.02x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.04 us: 1.01x faster                                                    |
| pickle_pure_python         | 365 us                                                                | 361 us: 1.01x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                                     |
| deepcopy                   | 446 us                                                                | 443 us: 1.01x faster                                                     |
| hexiom                     | 6.98 ms                                                               | 7.01 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 663 ms: 1.01x slower                                                     |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 8.47 ms: 1.01x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.6 us: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.22 sec: 1.01x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 128 ms: 1.01x slower                                                     |
| django_template            | 40.7 ms                                                               | 41.3 ms: 1.01x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.16 ms: 1.01x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 50.4 us: 1.02x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 27.9 ms: 1.02x slower                                                    |
| meteor_contest             | 112 ms                                                                | 114 ms: 1.02x slower                                                     |
| sympy_expand               | 454 ms                                                                | 463 ms: 1.02x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 62.6 ms: 1.02x slower                                                    |
| chameleon                  | 8.81 ms                                                               | 9.02 ms: 1.02x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 81.0 ms: 1.03x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.93 sec: 1.03x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.88 us: 1.03x slower                                                    |
| go                         | 157 ms                                                                | 162 ms: 1.03x slower                                                     |
| thrift                     | 937 us                                                                | 967 us: 1.03x slower                                                     |
| json                       | 5.54 ms                                                               | 5.73 ms: 1.03x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 953 ms: 1.04x slower                                                     |
| fannkuch                   | 443 ms                                                                | 463 ms: 1.04x slower                                                     |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.46 us: 1.05x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 68.4 ms: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.05x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.57 ms: 1.06x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.6 us: 1.06x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.94 ms: 1.07x slower                                                    |
| scimark_fft                | 418 ms                                                                | 446 ms: 1.07x slower                                                     |
| richards_super             | 58.5 ms                                                               | 62.4 ms: 1.07x slower                                                    |
| nbody                      | 105 ms                                                                | 112 ms: 1.07x slower                                                     |
| gunicorn                   | 1.14 ms                                                               | 1.21 ms: 1.07x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.7 us: 1.07x slower                                                    |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                     |
| richards                   | 50.9 ms                                                               | 54.9 ms: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.09x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 31.2 ms: 1.10x slower                                                    |
| python_startup             | 11.4 ms                                                               | 12.6 ms: 1.11x slower                                                    |
| coverage                   | 87.3 ms                                                               | 97.5 ms: 1.12x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.13 ms: 1.17x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.40 ms: 1.25x slower                                                    |
| telco                      | 8.51 ms                                                               | 164 ms: 19.26x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (15): pylint, tornado_http, xml_etree_parse, sqlglot_parse, async_generators, pyflate, nqueens, dask, coroutines, asyncio_tcp, pickle_dict, genshi_xml, regex_dna, xml_etree_generate, aiohttp
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: flaskblogging

# HPT report

- Reliability score: 71.71% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x