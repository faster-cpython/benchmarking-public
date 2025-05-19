# Results vs. 3.12.0

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-aarch64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.057x slower
- HPT reliability: 99.77%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 352 ms: 1.14x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.24 sec: 1.09x slower                                                  |
| html5lib       | 65.1 ms                                                               | 68.6 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 841 ms: 1.67x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 452 ms: 1.64x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 870 ms: 1.62x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 482 ms: 1.61x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 372 ms: 1.55x faster                                                    |
| async_tree_none            | 624 ms                                                                | 409 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 638 ms: 1.39x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 684 ms: 1.33x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 231 ms: 1.01x faster                                                    |
| float          | 92.1 ms                                                               | 95.5 ms: 1.04x slower                                                   |
| nbody          | 105 ms                                                                | 170 ms: 1.63x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.19x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.96 ms: 1.17x faster                                                   |
| regex_dna      | 254 ms                                                                | 238 ms: 1.07x faster                                                    |
| regex_compile  | 137 ms                                                                | 151 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 128 ms: 1.17x faster                                                    |
| xml_etree_parse      | 195 ms                                                                | 182 ms: 1.07x faster                                                    |
| pickle_list          | 5.25 us                                                               | 5.61 us: 1.07x slower                                                   |
| pickle_dict          | 37.3 us                                                               | 40.5 us: 1.08x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.84 sec: 1.09x slower                                                  |
| unpickle_list        | 6.17 us                                                               | 6.97 us: 1.13x slower                                                   |
| unpickle             | 18.5 us                                                               | 21.0 us: 1.14x slower                                                   |
| pickle               | 13.4 us                                                               | 15.4 us: 1.15x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 302 us: 1.16x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 428 us: 1.17x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 142 ms: 1.27x slower                                                    |
| json_loads           | 30.7 us                                                               | 39.0 us: 1.27x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 101 ms: 1.28x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.12x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.2 ms: 1.46x slower                                                   |
| python_startup         | 11.4 ms                                                               | 20.1 ms: 1.77x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.61x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 72.1 ms: 1.19x slower                                                   |
| django_template | 40.7 ms                                                               | 50.6 ms: 1.25x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 35.0 ms: 1.28x slower                                                   |
| mako            | 12.9 ms                                                               | 21.3 ms: 1.65x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.33x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.97 sec: 1.73x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 841 ms: 1.67x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 452 ms: 1.64x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 870 ms: 1.62x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 482 ms: 1.61x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 372 ms: 1.55x faster                                                    |
| gc_traversal               | 4.40 ms                                                               | 2.88 ms: 1.53x faster                                                   |
| async_tree_none            | 624 ms                                                                | 409 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 638 ms: 1.39x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 684 ms: 1.33x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 128 ms: 1.17x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.96 ms: 1.17x faster                                                   |
| deepcopy                   | 446 us                                                                | 386 us: 1.15x faster                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.46 us: 1.09x faster                                                   |
| generators                 | 43.5 ms                                                               | 40.3 ms: 1.08x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                    |
| regex_dna                  | 254 ms                                                                | 238 ms: 1.07x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 23.6 ms: 1.04x faster                                                   |
| deepcopy_memo              | 49.6 us                                                               | 48.1 us: 1.03x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 61.1 ms: 1.01x faster                                                   |
| pidigits                   | 233 ms                                                                | 231 ms: 1.01x faster                                                    |
| async_generators           | 491 ms                                                                | 498 ms: 1.02x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 670 ms: 1.02x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.18 us: 1.02x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 582 ms: 1.03x slower                                                    |
| float                      | 92.1 ms                                                               | 95.5 ms: 1.04x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 30.3 ms: 1.04x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 68.6 ms: 1.05x slower                                                   |
| scimark_sor                | 150 ms                                                                | 159 ms: 1.06x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.61 us: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                    |
| pyflate                    | 559 ms                                                                | 600 ms: 1.07x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.35 sec: 1.08x slower                                                  |
| pylint                     | 355 ms                                                                | 383 ms: 1.08x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 40.5 us: 1.08x slower                                                   |
| raytrace                   | 353 ms                                                                | 383 ms: 1.08x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.24 sec: 1.09x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 2.84 sec: 1.09x slower                                                  |
| regex_compile              | 137 ms                                                                | 151 ms: 1.10x slower                                                    |
| scimark_fft                | 418 ms                                                                | 460 ms: 1.10x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.41 sec: 1.10x slower                                                  |
| chaos                      | 71.4 ms                                                               | 78.9 ms: 1.10x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.97 us: 1.13x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.68 ms: 1.14x slower                                                   |
| unpickle                   | 18.5 us                                                               | 21.0 us: 1.14x slower                                                   |
| 2to3                       | 308 ms                                                                | 352 ms: 1.14x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.4 us: 1.15x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 302 us: 1.16x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.07 sec: 1.17x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.20 sec: 1.17x slower                                                  |
| nqueens                    | 99.2 ms                                                               | 116 ms: 1.17x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 428 us: 1.17x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 8.24 ms: 1.18x slower                                                   |
| logging_simple             | 7.63 us                                                               | 9.07 us: 1.19x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 72.1 ms: 1.19x slower                                                   |
| json                       | 5.54 ms                                                               | 6.63 ms: 1.20x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 25.9 ms: 1.20x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.30 ms: 1.20x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 175 ms: 1.20x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 188 ms: 1.21x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 103 ms: 1.21x slower                                                    |
| logging_format             | 8.34 us                                                               | 10.1 us: 1.22x slower                                                   |
| sympy_str                  | 280 ms                                                                | 343 ms: 1.23x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.67 ms: 1.24x slower                                                   |
| thrift                     | 937 us                                                                | 1.16 ms: 1.24x slower                                                   |
| django_template            | 40.7 ms                                                               | 50.6 ms: 1.25x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 142 ms: 1.27x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 110 ms: 1.27x slower                                                    |
| json_loads                 | 30.7 us                                                               | 39.0 us: 1.27x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 35.0 ms: 1.28x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 101 ms: 1.28x slower                                                    |
| sympy_expand               | 454 ms                                                                | 581 ms: 1.28x slower                                                    |
| telco                      | 8.51 ms                                                               | 11.3 ms: 1.33x slower                                                   |
| richards_super             | 58.5 ms                                                               | 78.3 ms: 1.34x slower                                                   |
| richards                   | 50.9 ms                                                               | 68.3 ms: 1.34x slower                                                   |
| meteor_contest             | 112 ms                                                                | 151 ms: 1.35x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.81 ms: 1.38x slower                                                   |
| fannkuch                   | 443 ms                                                                | 618 ms: 1.39x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.2 ms: 1.46x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 271 us: 1.50x slower                                                    |
| nbody                      | 105 ms                                                                | 170 ms: 1.63x slower                                                    |
| mako                       | 12.9 ms                                                               | 21.3 ms: 1.65x slower                                                   |
| coverage                   | 87.3 ms                                                               | 146 ms: 1.68x slower                                                    |
| python_startup             | 11.4 ms                                                               | 20.1 ms: 1.77x slower                                                   |
| logging_silent             | 127 ns                                                                | 765 ns: 6.03x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 62.3 ms: 8.84x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (3): regex_v8, go, comprehensions
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250518-3.15.0a0-009e7b3-NOGIL/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.057x slower

# HPT report

- Reliability score: 99.77% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.31x