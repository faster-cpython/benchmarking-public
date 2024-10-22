# Results vs. 3.12.0

- fork: colesbury
- ref: gh_100240_freelist
- machine: linux-aarch64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.03x faster
- HPT reliability: 94.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 302 ms: 1.02x faster                                                     |
| docutils       | 2.98 sec                                                              | 3.08 sec: 1.03x slower                                                   |
| html5lib       | 65.1 ms                                                               | 66.6 ms: 1.02x slower                                                    |
| tornado_http   | 136 ms                                                                | 126 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 406 ms: 1.42x faster                                                     |
| async_tree_none            | 624 ms                                                                | 439 ms: 1.42x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 550 ms: 1.41x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 536 ms: 1.38x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.08 sec: 1.30x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.27x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 724 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 705 ms: 1.25x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.34x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                     |
| float          | 92.1 ms                                                               | 93.0 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 112 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 129 ms: 1.06x faster                                                     |
| regex_dna      | 254 ms                                                                | 250 ms: 1.02x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.87 ms: 1.05x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                                   |
| pickle_pure_python   | 365 us                                                                | 359 us: 1.02x faster                                                     |
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                                     |
| json_loads           | 30.7 us                                                               | 32.3 us: 1.05x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.76 ms: 1.05x slower                                                    |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.8 ms: 1.01x slower                                                    |
| mako            | 12.9 ms                                                               | 13.4 ms: 1.03x slower                                                    |
| django_template | 40.7 ms                                                               | 42.8 ms: 1.05x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 406 ms: 1.42x faster                                                     |
| async_tree_none            | 624 ms                                                                | 439 ms: 1.42x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 550 ms: 1.41x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 536 ms: 1.38x faster                                                     |
| deepcopy                   | 446 us                                                                | 331 us: 1.35x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.08 sec: 1.30x faster                                                   |
| deepcopy_memo              | 49.6 us                                                               | 38.5 us: 1.29x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.27x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 724 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 705 ms: 1.25x faster                                                     |
| comprehensions             | 25.4 us                                                               | 20.6 us: 1.23x faster                                                    |
| raytrace                   | 353 ms                                                                | 297 ms: 1.19x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.51 us: 1.17x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.2 ms: 1.16x faster                                                    |
| generators                 | 43.5 ms                                                               | 37.8 ms: 1.15x faster                                                    |
| tornado_http               | 136 ms                                                                | 126 ms: 1.08x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.07 us: 1.08x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.76 us: 1.07x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.85 ms: 1.07x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.72 ms: 1.07x faster                                                    |
| regex_compile              | 137 ms                                                                | 129 ms: 1.06x faster                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 81.6 ms: 1.06x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.23 ms: 1.06x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                                     |
| sympy_str                  | 280 ms                                                                | 266 ms: 1.05x faster                                                     |
| chaos                      | 71.4 ms                                                               | 68.0 ms: 1.05x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.40 ms: 1.04x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.4 ms: 1.03x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                     |
| mdp                        | 3.41 sec                                                              | 3.31 sec: 1.03x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                   |
| 2to3                       | 308 ms                                                                | 302 ms: 1.02x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                                   |
| pickle_pure_python         | 365 us                                                                | 359 us: 1.02x faster                                                     |
| regex_dna                  | 254 ms                                                                | 250 ms: 1.02x faster                                                     |
| asyncio_tcp                | 566 ms                                                                | 560 ms: 1.01x faster                                                     |
| async_generators           | 491 ms                                                                | 487 ms: 1.01x faster                                                     |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                     |
| coroutines                 | 29.0 ms                                                               | 28.8 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.17 sec: 1.01x faster                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                     |
| sympy_expand               | 454 ms                                                                | 457 ms: 1.01x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 7.04 ms: 1.01x slower                                                    |
| richards_super             | 58.5 ms                                                               | 59.0 ms: 1.01x slower                                                    |
| float                      | 92.1 ms                                                               | 93.0 ms: 1.01x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.90 sec: 1.01x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 27.8 ms: 1.01x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 931 ms: 1.02x slower                                                     |
| go                         | 157 ms                                                                | 161 ms: 1.02x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 66.6 ms: 1.02x slower                                                    |
| json                       | 5.54 ms                                                               | 5.69 ms: 1.03x slower                                                    |
| thrift                     | 937 us                                                                | 964 us: 1.03x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.08 sec: 1.03x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 103 ms: 1.03x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.41 ms: 1.03x slower                                                    |
| richards                   | 50.9 ms                                                               | 52.8 ms: 1.04x slower                                                    |
| fannkuch                   | 443 ms                                                                | 461 ms: 1.04x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 8.76 ms: 1.05x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.87 ms: 1.05x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                    |
| django_template            | 40.7 ms                                                               | 42.8 ms: 1.05x slower                                                    |
| scimark_fft                | 418 ms                                                                | 441 ms: 1.05x slower                                                     |
| logging_silent             | 127 ns                                                                | 134 ns: 1.05x slower                                                     |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                                     |
| nbody                      | 105 ms                                                                | 112 ms: 1.07x slower                                                     |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 200 us: 1.11x slower                                                     |
| gc_traversal               | 4.40 ms                                                               | 4.93 ms: 1.12x slower                                                    |
| coverage                   | 87.3 ms                                                               | 100.0 ms: 1.14x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.94 ms: 1.17x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.30 ms: 1.20x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                             |

Benchmark hidden because not significant (12): pylint, dulwich_log, bench_mp_pool, genshi_xml, pyflate, meteor_contest, xml_etree_parse, asyncio_websockets, xml_etree_iterparse, xml_etree_process, sqlglot_normalize, sqlglot_optimize
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240717-3.14.0a0-85453d0/bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0.json: bpe_tokeniser

# HPT report

- Reliability score: 94.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x