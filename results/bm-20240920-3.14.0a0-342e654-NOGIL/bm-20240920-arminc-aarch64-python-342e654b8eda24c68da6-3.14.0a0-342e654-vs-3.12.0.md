# Results vs. 3.12.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-aarch64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.49x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 508 ms: 1.65x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.93 sec: 1.32x slower                                                  |
| html5lib       | 65.1 ms                                                               | 118 ms: 1.82x slower                                                    |
| tornado_http   | 136 ms                                                                | 203 ms: 1.50x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.56x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 689 ms: 1.07x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 735 ms: 1.06x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.34 sec: 1.05x faster                                                  |
| async_tree_io              | 1.41 sec                                                              | 1.37 sec: 1.03x faster                                                  |
| async_tree_none            | 624 ms                                                                | 604 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 862 ms: 1.03x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 565 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 897 ms: 1.02x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 205 ms: 2.22x slower                                                    |
| nbody          | 105 ms                                                                | 279 ms: 2.67x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.82x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.42 ms: 1.05x faster                                                   |
| regex_v8       | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                                   |
| regex_compile  | 137 ms                                                                | 248 ms: 1.80x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.19x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 182 ms: 1.07x faster                                                    |
| pickle               | 13.4 us                                                               | 13.1 us: 1.03x faster                                                   |
| pickle_list          | 5.25 us                                                               | 5.41 us: 1.03x slower                                                   |
| pickle_dict          | 37.3 us                                                               | 39.4 us: 1.05x slower                                                   |
| unpickle             | 18.5 us                                                               | 21.3 us: 1.15x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 7.12 us: 1.15x slower                                                   |
| json_loads           | 30.7 us                                                               | 37.9 us: 1.24x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 155 ms: 1.38x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 17.8 ms: 1.46x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 4.11 sec: 1.59x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 125 ms: 1.59x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 526 us: 2.02x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 754 us: 2.07x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.29x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.1 ms: 1.45x slower                                                   |
| python_startup         | 11.4 ms                                                               | 18.1 ms: 1.60x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.52x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 101 ms: 1.67x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 52.1 ms: 1.90x slower                                                   |
| django_template | 40.7 ms                                                               | 79.0 ms: 1.94x slower                                                   |
| mako            | 12.9 ms                                                               | 28.4 ms: 2.20x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.92x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 3.44 ms: 1.28x faster                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 1.61 ms: 1.19x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 689 ms: 1.07x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 735 ms: 1.06x faster                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 6.69 ms: 1.05x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.34 sec: 1.05x faster                                                  |
| regex_effbot               | 4.64 ms                                                               | 4.42 ms: 1.05x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.37 sec: 1.03x faster                                                  |
| async_tree_none            | 624 ms                                                                | 604 ms: 1.03x faster                                                    |
| pickle                     | 13.4 us                                                               | 13.1 us: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 862 ms: 1.03x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 565 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 897 ms: 1.02x faster                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 676 ms: 1.03x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.41 us: 1.03x slower                                                   |
| pathlib                    | 24.5 ms                                                               | 25.7 ms: 1.05x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 39.4 us: 1.05x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 4.08 us: 1.08x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                                   |
| unpickle                   | 18.5 us                                                               | 21.3 us: 1.15x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 7.12 us: 1.15x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 668 ms: 1.18x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.59 sec: 1.19x slower                                                  |
| deepcopy                   | 446 us                                                                | 531 us: 1.19x slower                                                    |
| json                       | 5.54 ms                                                               | 6.77 ms: 1.22x slower                                                   |
| json_loads                 | 30.7 us                                                               | 37.9 us: 1.24x slower                                                   |
| mdp                        | 3.41 sec                                                              | 4.28 sec: 1.25x slower                                                  |
| docutils                   | 2.98 sec                                                              | 3.93 sec: 1.32x slower                                                  |
| generators                 | 43.5 ms                                                               | 57.8 ms: 1.33x slower                                                   |
| async_generators           | 491 ms                                                                | 653 ms: 1.33x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 39.3 ms: 1.35x slower                                                   |
| deepcopy_memo              | 49.6 us                                                               | 67.9 us: 1.37x slower                                                   |
| scimark_fft                | 418 ms                                                                | 574 ms: 1.37x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 155 ms: 1.38x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.66 ms: 1.40x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 5.76 us: 1.41x slower                                                   |
| pylint                     | 355 ms                                                                | 499 ms: 1.41x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.1 ms: 1.45x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 17.8 ms: 1.46x slower                                                   |
| meteor_contest             | 112 ms                                                                | 166 ms: 1.48x slower                                                    |
| tornado_http               | 136 ms                                                                | 203 ms: 1.50x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 149 ms: 1.50x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 93.6 ms: 1.51x slower                                                   |
| telco                      | 8.51 ms                                                               | 12.9 ms: 1.51x slower                                                   |
| coverage                   | 87.3 ms                                                               | 133 ms: 1.53x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 2.01 ms: 1.54x slower                                                   |
| comprehensions             | 25.4 us                                                               | 40.2 us: 1.58x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 4.11 sec: 1.59x slower                                                  |
| xml_etree_process          | 79.0 ms                                                               | 125 ms: 1.59x slower                                                    |
| python_startup             | 11.4 ms                                                               | 18.1 ms: 1.60x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 2.00 sec: 1.60x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 34.6 ms: 1.60x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 139 ms: 1.60x slower                                                    |
| 2to3                       | 308 ms                                                                | 508 ms: 1.65x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 101 ms: 1.67x slower                                                    |
| fannkuch                   | 443 ms                                                                | 753 ms: 1.70x slower                                                    |
| spectral_norm              | 131 ms                                                                | 225 ms: 1.72x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 217 ms: 1.73x slower                                                    |
| thrift                     | 937 us                                                                | 1.62 ms: 1.73x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 110 ms: 1.79x slower                                                    |
| pyflate                    | 559 ms                                                                | 1.00 sec: 1.79x slower                                                  |
| typing_runtime_protocols   | 181 us                                                                | 324 us: 1.80x slower                                                    |
| sympy_str                  | 280 ms                                                                | 504 ms: 1.80x slower                                                    |
| regex_compile              | 137 ms                                                                | 248 ms: 1.80x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 118 ms: 1.82x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.67 sec: 1.82x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 3.43 sec: 1.82x slower                                                  |
| logging_simple             | 7.63 us                                                               | 14.1 us: 1.84x slower                                                   |
| logging_format             | 8.34 us                                                               | 15.4 us: 1.84x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 52.1 ms: 1.90x slower                                                   |
| django_template            | 40.7 ms                                                               | 79.0 ms: 1.94x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 310 ms: 2.00x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 526 us: 2.02x slower                                                    |
| sympy_expand               | 454 ms                                                                | 936 ms: 2.06x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 754 us: 2.07x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 176 ms: 2.07x slower                                                    |
| mako                       | 12.9 ms                                                               | 28.4 ms: 2.20x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 15.4 ms: 2.20x slower                                                   |
| float                      | 92.1 ms                                                               | 205 ms: 2.22x slower                                                    |
| logging_silent             | 127 ns                                                                | 284 ns: 2.24x slower                                                    |
| scimark_sor                | 150 ms                                                                | 337 ms: 2.25x slower                                                    |
| chaos                      | 71.4 ms                                                               | 161 ms: 2.26x slower                                                    |
| richards                   | 50.9 ms                                                               | 115 ms: 2.26x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 330 ms: 2.27x slower                                                    |
| richards_super             | 58.5 ms                                                               | 135 ms: 2.31x slower                                                    |
| raytrace                   | 353 ms                                                                | 821 ms: 2.32x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 4.28 ms: 2.34x slower                                                   |
| go                         | 157 ms                                                                | 384 ms: 2.44x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 3.72 ms: 2.54x slower                                                   |
| nbody                      | 105 ms                                                                | 279 ms: 2.67x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 12.4 ms: 3.01x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.49x slower                                                            |

Benchmark hidden because not significant (2): regex_dna, xml_etree_iterparse
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240920-3.14.0a0-342e654-NOGIL/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.44x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.35x

# Memory
- memory change: 1.08x