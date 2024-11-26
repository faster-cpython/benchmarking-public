# Results vs. 3.12.0

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: linux-aarch64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.078x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 382 ms: 1.24x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.93 sec: 1.32x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.2 ms: 1.09x slower                                                   |
| tornado_http   | 136 ms                                                                | 146 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 440 ms: 1.42x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 435 ms: 1.33x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 588 ms: 1.32x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 561 ms: 1.32x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 749 ms: 1.22x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.21x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 746 ms: 1.18x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.27x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.4 ms: 1.05x faster                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 113 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                   |
| regex_compile  | 137 ms                                                                | 194 ms: 1.41x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 112 ms                                                                | 109 ms: 1.03x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                  |
| unpickle_pure_python | 260 us                                                                | 265 us: 1.02x slower                                                    |
| json_loads           | 30.7 us                                                               | 31.4 us: 1.02x slower                                                   |
| pickle_dict          | 37.3 us                                                               | 38.3 us: 1.02x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.36 us: 1.03x slower                                                   |
| pickle               | 13.4 us                                                               | 13.9 us: 1.04x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.5 us: 1.05x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 404 us: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_list, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.73 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                   |
| django_template | 40.7 ms                                                               | 51.7 ms: 1.27x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 35.1 ms: 1.28x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 80.8 ms: 1.33x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.22x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 440 ms: 1.42x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 435 ms: 1.33x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 588 ms: 1.32x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 561 ms: 1.32x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 39.8 us: 1.25x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 749 ms: 1.22x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.21x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 746 ms: 1.18x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.4 ms: 1.15x faster                                                   |
| deepcopy                   | 446 us                                                                | 417 us: 1.07x faster                                                    |
| float                      | 92.1 ms                                                               | 87.4 ms: 1.05x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.93 us: 1.04x faster                                                   |
| comprehensions             | 25.4 us                                                               | 24.7 us: 1.03x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 109 ms: 1.03x faster                                                    |
| raytrace                   | 353 ms                                                                | 346 ms: 1.02x faster                                                    |
| logging_format             | 8.34 us                                                               | 8.21 us: 1.02x faster                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                  |
| sqlite_synth               | 3.77 us                                                               | 3.82 us: 1.01x slower                                                   |
| scimark_sor                | 150 ms                                                                | 152 ms: 1.01x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 265 us: 1.02x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.48 sec: 1.02x slower                                                  |
| bench_thread_pool          | 1.31 ms                                                               | 1.34 ms: 1.02x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 149 ms: 1.02x slower                                                    |
| json_loads                 | 30.7 us                                                               | 31.4 us: 1.02x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 38.3 us: 1.02x slower                                                   |
| json                       | 5.54 ms                                                               | 5.71 ms: 1.03x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.25 sec: 1.03x slower                                                  |
| thrift                     | 937 us                                                                | 966 us: 1.03x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.36 us: 1.03x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 89.4 ms: 1.03x slower                                                   |
| pickle                     | 13.4 us                                                               | 13.9 us: 1.04x slower                                                   |
| async_generators           | 491 ms                                                                | 510 ms: 1.04x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.73 ms: 1.04x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.5 us: 1.05x slower                                                   |
| logging_silent             | 127 ns                                                                | 135 ns: 1.06x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.53 ms: 1.07x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.40 ms: 1.07x slower                                                   |
| tornado_http               | 136 ms                                                                | 146 ms: 1.08x slower                                                    |
| nbody                      | 105 ms                                                                | 113 ms: 1.08x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| scimark_fft                | 418 ms                                                                | 458 ms: 1.09x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 71.2 ms: 1.09x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.81 ms: 1.10x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 627 ms: 1.11x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 404 us: 1.11x slower                                                    |
| meteor_contest             | 112 ms                                                                | 125 ms: 1.12x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 95.3 ms: 1.12x slower                                                   |
| spectral_norm              | 131 ms                                                                | 147 ms: 1.12x slower                                                    |
| fannkuch                   | 443 ms                                                                | 505 ms: 1.14x slower                                                    |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.16x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 213 us: 1.18x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.73 ms: 1.18x slower                                                   |
| pyflate                    | 559 ms                                                                | 664 ms: 1.19x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.27 ms: 1.20x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 151 ms: 1.20x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.30 ms: 1.20x slower                                                   |
| go                         | 157 ms                                                                | 189 ms: 1.20x slower                                                    |
| telco                      | 8.51 ms                                                               | 10.3 ms: 1.21x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.20 ms: 1.21x slower                                                   |
| 2to3                       | 308 ms                                                                | 382 ms: 1.24x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.56 sec: 1.24x slower                                                  |
| django_template            | 40.7 ms                                                               | 51.7 ms: 1.27x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 78.3 ms: 1.28x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 127 ms: 1.28x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 35.1 ms: 1.28x slower                                                   |
| chaos                      | 71.4 ms                                                               | 92.3 ms: 1.29x slower                                                   |
| richards_super             | 58.5 ms                                                               | 75.9 ms: 1.30x slower                                                   |
| sympy_str                  | 280 ms                                                                | 366 ms: 1.31x slower                                                    |
| generators                 | 43.5 ms                                                               | 57.0 ms: 1.31x slower                                                   |
| richards                   | 50.9 ms                                                               | 67.0 ms: 1.32x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.93 sec: 1.32x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 28.5 ms: 1.32x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 80.8 ms: 1.33x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 83.2 ms: 1.34x slower                                                   |
| pylint                     | 355 ms                                                                | 477 ms: 1.34x slower                                                    |
| sympy_expand               | 454 ms                                                                | 613 ms: 1.35x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 211 ms: 1.37x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.26 sec: 1.37x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.64 sec: 1.40x slower                                                  |
| regex_compile              | 137 ms                                                                | 194 ms: 1.41x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.2 ms: 1.47x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.08x slower                                                            |

Benchmark hidden because not significant (8): xml_etree_parse, logging_simple, coroutines, pickle_list, regex_dna, xml_etree_iterparse, asyncio_websockets, xml_etree_process
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240924-3.14.0a0-54dd77f-JIT/bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f.json: bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.078x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x