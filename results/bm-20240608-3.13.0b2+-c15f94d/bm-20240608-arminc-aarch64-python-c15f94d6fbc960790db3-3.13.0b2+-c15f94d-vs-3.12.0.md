# Results vs. 3.12.0

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-aarch64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.01x faster
- HPT reliability: 77.43%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| chameleon      | 8.81 ms                                                               | 8.94 ms: 1.01x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                   |
| html5lib       | 65.1 ms                                                               | 66.1 ms: 1.02x slower                                                    |
| tornado_http   | 136 ms                                                                | 126 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 490 ms: 1.27x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 604 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 474 ms: 1.22x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 645 ms: 1.20x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 761 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 792 ms: 1.15x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.19x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                     |
| nbody          | 105 ms                                                                | 113 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 129 ms: 1.06x faster                                                     |
| regex_dna      | 254 ms                                                                | 249 ms: 1.02x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.89 ms: 1.06x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 253 us: 1.03x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                   |
| pickle               | 13.4 us                                                               | 13.6 us: 1.01x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 38.0 us: 1.02x slower                                                    |
| pickle_list          | 5.25 us                                                               | 5.35 us: 1.02x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 81.7 ms: 1.03x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 117 ms: 1.04x slower                                                     |
| json_loads           | 30.7 us                                                               | 32.0 us: 1.04x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.47 us: 1.05x slower                                                    |
| unpickle             | 18.5 us                                                               | 19.6 us: 1.06x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.71 ms: 1.04x slower                                                    |
| python_startup         | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.6 ms: 1.01x slower                                                    |
| mako            | 12.9 ms                                                               | 13.5 ms: 1.04x slower                                                    |
| django_template | 40.7 ms                                                               | 42.7 ms: 1.05x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 490 ms: 1.27x faster                                                     |
| comprehensions             | 25.4 us                                                               | 20.1 us: 1.26x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 604 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 474 ms: 1.22x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 645 ms: 1.20x faster                                                     |
| raytrace                   | 353 ms                                                                | 299 ms: 1.18x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.16x faster                                                   |
| generators                 | 43.5 ms                                                               | 37.4 ms: 1.16x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 761 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 792 ms: 1.15x faster                                                     |
| mypy2                      | 873 ms                                                                | 759 ms: 1.15x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 22.6 ms: 1.09x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.06 us: 1.08x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.75 us: 1.08x faster                                                    |
| tornado_http               | 136 ms                                                                | 126 ms: 1.08x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.85 ms: 1.07x faster                                                    |
| regex_compile              | 137 ms                                                                | 129 ms: 1.06x faster                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 81.6 ms: 1.06x faster                                                    |
| chaos                      | 71.4 ms                                                               | 67.8 ms: 1.05x faster                                                    |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.40 ms: 1.04x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.75 ms: 1.04x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.6 ms: 1.04x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.21 sec: 1.04x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 141 ms: 1.03x faster                                                     |
| mdp                        | 3.41 sec                                                              | 3.31 sec: 1.03x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 253 us: 1.03x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 4.00 us: 1.02x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.28 ms: 1.02x faster                                                    |
| regex_dna                  | 254 ms                                                                | 249 ms: 1.02x faster                                                     |
| dulwich_log                | 62.0 ms                                                               | 61.0 ms: 1.02x faster                                                    |
| pyflate                    | 559 ms                                                                | 554 ms: 1.01x faster                                                     |
| async_generators           | 491 ms                                                                | 486 ms: 1.01x faster                                                     |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 27.6 ms: 1.01x slower                                                    |
| fannkuch                   | 443 ms                                                                | 447 ms: 1.01x slower                                                     |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 127 ms: 1.01x slower                                                     |
| deepcopy_memo              | 49.6 us                                                               | 50.1 us: 1.01x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 62.0 ms: 1.01x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.6 us: 1.01x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.06 ms: 1.01x slower                                                    |
| chameleon                  | 8.81 ms                                                               | 8.94 ms: 1.01x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 66.1 ms: 1.02x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 38.0 us: 1.02x slower                                                    |
| json                       | 5.54 ms                                                               | 5.64 ms: 1.02x slower                                                    |
| sympy_expand               | 454 ms                                                                | 462 ms: 1.02x slower                                                     |
| pickle_list                | 5.25 us                                                               | 5.35 us: 1.02x slower                                                    |
| go                         | 157 ms                                                                | 161 ms: 1.02x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.93 sec: 1.02x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 7.22 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.24 sec: 1.03x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 943 ms: 1.03x slower                                                     |
| thrift                     | 937 us                                                                | 967 us: 1.03x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 81.7 ms: 1.03x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 586 ms: 1.04x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.91 us: 1.04x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 117 ms: 1.04x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 8.71 ms: 1.04x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.0 us: 1.04x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.5 ms: 1.04x slower                                                    |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.47 us: 1.05x slower                                                    |
| django_template            | 40.7 ms                                                               | 42.7 ms: 1.05x slower                                                    |
| aiohttp                    | 1.16 ms                                                               | 1.22 ms: 1.05x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.89 ms: 1.06x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.6 us: 1.06x slower                                                    |
| richards_super             | 58.5 ms                                                               | 62.2 ms: 1.06x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 192 us: 1.06x slower                                                     |
| scimark_fft                | 418 ms                                                                | 446 ms: 1.06x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.66 ms: 1.08x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                    |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                     |
| scimark_sor                | 150 ms                                                                | 161 ms: 1.08x slower                                                     |
| nbody                      | 105 ms                                                                | 113 ms: 1.08x slower                                                     |
| richards                   | 50.9 ms                                                               | 55.4 ms: 1.09x slower                                                    |
| gunicorn                   | 1.14 ms                                                               | 1.24 ms: 1.09x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                    |
| coverage                   | 87.3 ms                                                               | 98.0 ms: 1.12x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.04 ms: 1.15x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.86 ms: 1.16x slower                                                    |
| python_startup             | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.34 ms: 1.22x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (12): pylint, xml_etree_iterparse, dask, 2to3, xml_etree_parse, float, asyncio_websockets, nqueens, deepcopy, pickle_pure_python, coroutines, genshi_xml
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: flaskblogging

# HPT report

- Reliability score: 77.43% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x