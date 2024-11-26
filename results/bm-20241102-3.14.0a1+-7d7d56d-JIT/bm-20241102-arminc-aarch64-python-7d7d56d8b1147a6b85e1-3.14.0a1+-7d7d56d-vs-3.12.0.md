# Results vs. 3.12.0

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: linux-aarch64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.088x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 405 ms: 1.31x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.74 sec: 1.25x slower                                                   |
| html5lib       | 65.1 ms                                                               | 76.8 ms: 1.18x slower                                                    |
| tornado_http   | 136 ms                                                                | 150 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.21x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 552 ms: 1.34x faster                                                     |
| async_tree_none            | 624 ms                                                                | 475 ms: 1.31x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 459 ms: 1.26x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 630 ms: 1.23x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 777 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 779 ms: 1.13x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.21x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 95.8 ms: 1.04x slower                                                    |
| pidigits       | 233 ms                                                                | 249 ms: 1.07x slower                                                     |
| nbody          | 105 ms                                                                | 116 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 5.09 ms: 1.10x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 32.3 ms: 1.14x slower                                                    |
| regex_compile  | 137 ms                                                                | 177 ms: 1.29x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate   | 112 ms                                                                | 110 ms: 1.02x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 81.9 ms: 1.04x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.7 us: 1.07x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 279 us: 1.07x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 403 us: 1.10x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.12 ms: 1.09x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.6 ms: 1.06x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 33.5 ms: 1.22x slower                                                    |
| django_template | 40.7 ms                                                               | 51.9 ms: 1.28x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 81.5 ms: 1.34x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.22x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 552 ms: 1.34x faster                                                     |
| async_tree_none            | 624 ms                                                                | 475 ms: 1.31x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 459 ms: 1.26x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 630 ms: 1.23x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.18x faster                                                   |
| deepcopy_memo              | 49.6 us                                                               | 42.1 us: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 777 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 779 ms: 1.13x faster                                                     |
| deepcopy                   | 446 us                                                                | 395 us: 1.13x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 110 ms: 1.02x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 87.2 ms: 1.03x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 677 ms: 1.03x slower                                                     |
| json                       | 5.54 ms                                                               | 5.73 ms: 1.03x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 81.9 ms: 1.04x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.28 ms: 1.04x slower                                                    |
| float                      | 92.1 ms                                                               | 95.8 ms: 1.04x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 152 ms: 1.04x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.59 sec: 1.05x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.06x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.39 ms: 1.06x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.7 us: 1.07x slower                                                    |
| pidigits                   | 233 ms                                                                | 249 ms: 1.07x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 279 us: 1.07x slower                                                     |
| scimark_fft                | 418 ms                                                                | 450 ms: 1.08x slower                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 93.6 ms: 1.08x slower                                                    |
| thrift                     | 937 us                                                                | 1.02 ms: 1.08x slower                                                    |
| scimark_sor                | 150 ms                                                                | 163 ms: 1.09x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 9.12 ms: 1.09x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.11 us: 1.09x slower                                                    |
| logging_silent             | 127 ns                                                                | 138 ns: 1.09x slower                                                     |
| async_generators           | 491 ms                                                                | 537 ms: 1.09x slower                                                     |
| regex_effbot               | 4.64 ms                                                               | 5.09 ms: 1.10x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 403 us: 1.10x slower                                                     |
| nbody                      | 105 ms                                                                | 116 ms: 1.11x slower                                                     |
| tornado_http               | 136 ms                                                                | 150 ms: 1.11x slower                                                     |
| pyflate                    | 559 ms                                                                | 627 ms: 1.12x slower                                                     |
| generators                 | 43.5 ms                                                               | 49.2 ms: 1.13x slower                                                    |
| fannkuch                   | 443 ms                                                                | 505 ms: 1.14x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 32.3 ms: 1.14x slower                                                    |
| meteor_contest             | 112 ms                                                                | 127 ms: 1.14x slower                                                     |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.15x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.70 ms: 1.16x slower                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 19.6 ms: 1.18x slower                                                    |
| spectral_norm              | 131 ms                                                                | 154 ms: 1.18x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 76.8 ms: 1.18x slower                                                    |
| chaos                      | 71.4 ms                                                               | 84.3 ms: 1.18x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.33 ms: 1.18x slower                                                    |
| go                         | 157 ms                                                                | 187 ms: 1.19x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.51 sec: 1.20x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.22 ms: 1.21x slower                                                    |
| richards_super             | 58.5 ms                                                               | 71.2 ms: 1.22x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 33.5 ms: 1.22x slower                                                    |
| telco                      | 8.51 ms                                                               | 10.4 ms: 1.22x slower                                                    |
| richards                   | 50.9 ms                                                               | 63.6 ms: 1.25x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 157 ms: 1.25x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.74 sec: 1.25x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 228 us: 1.26x slower                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 200 ms: 1.27x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 126 ms: 1.27x slower                                                     |
| django_template            | 40.7 ms                                                               | 51.9 ms: 1.28x slower                                                    |
| regex_compile              | 137 ms                                                                | 177 ms: 1.29x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 80.4 ms: 1.30x slower                                                    |
| 2to3                       | 308 ms                                                                | 405 ms: 1.31x slower                                                     |
| sympy_str                  | 280 ms                                                                | 368 ms: 1.32x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 81.5 ms: 1.34x slower                                                    |
| sympy_expand               | 454 ms                                                                | 613 ms: 1.35x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.25 sec: 1.36x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 85.3 ms: 1.39x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.62 sec: 1.39x slower                                                   |
| pylint                     | 355 ms                                                                | 497 ms: 1.40x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 9.97 ms: 1.43x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 225 ms: 1.46x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 31.6 ms: 1.46x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.72 ms: 1.53x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.85 ms: 2.00x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.63 sec: 231.29x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.19x slower                                                             |

Benchmark hidden because not significant (10): pathlib, xml_etree_parse, xml_etree_iterparse, regex_dna, deepcopy_reduce, comprehensions, logging_format, raytrace, coroutines, logging_simple
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.088x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x