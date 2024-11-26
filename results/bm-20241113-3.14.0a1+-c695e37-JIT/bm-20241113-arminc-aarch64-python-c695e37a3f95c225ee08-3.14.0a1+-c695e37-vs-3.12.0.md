# Results vs. 3.12.0

- fork: python
- ref: c695e37a3f95c225ee08
- machine: linux-aarch64
- commit hash: c695e37
- commit date: 2024-11-13
- overall geometric mean: 1.087x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 398 ms: 1.29x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.79 sec: 1.27x slower                                                   |
| html5lib       | 65.1 ms                                                               | 73.7 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.23x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 557 ms: 1.33x faster                                                     |
| async_tree_none            | 624 ms                                                                | 477 ms: 1.31x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 618 ms: 1.26x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 465 ms: 1.24x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.19x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 765 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 790 ms: 1.15x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.09x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.21x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 94.6 ms: 1.03x slower                                                    |
| nbody          | 105 ms                                                                | 116 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 5.20 ms: 1.12x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 33.6 ms: 1.18x slower                                                    |
| regex_compile  | 137 ms                                                                | 180 ms: 1.31x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.15x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 270 us: 1.04x slower                                                     |
| xml_etree_process    | 79.0 ms                                                               | 82.6 ms: 1.05x slower                                                    |
| json_loads           | 30.7 us                                                               | 33.1 us: 1.08x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 399 us: 1.09x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.03 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 33.6 ms: 1.23x slower                                                    |
| django_template | 40.7 ms                                                               | 52.5 ms: 1.29x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 84.6 ms: 1.40x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.23x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 557 ms: 1.33x faster                                                     |
| async_tree_none            | 624 ms                                                                | 477 ms: 1.31x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 618 ms: 1.26x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 465 ms: 1.24x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 40.8 us: 1.22x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.19x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 765 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 790 ms: 1.15x faster                                                     |
| deepcopy                   | 446 us                                                                | 399 us: 1.12x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.09x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 22.8 ms: 1.08x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                   |
| float                      | 92.1 ms                                                               | 94.6 ms: 1.03x slower                                                    |
| json                       | 5.54 ms                                                               | 5.74 ms: 1.04x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 683 ms: 1.04x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.4 ms: 1.04x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 270 us: 1.04x slower                                                     |
| raytrace                   | 353 ms                                                                | 368 ms: 1.04x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 4.30 ms: 1.04x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 82.6 ms: 1.05x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 90.8 ms: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.65 sec: 1.07x slower                                                   |
| logging_silent             | 127 ns                                                                | 136 ns: 1.07x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.41 ms: 1.08x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 91.6 ms: 1.08x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.1 us: 1.08x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.03 ms: 1.08x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.07 us: 1.08x slower                                                    |
| async_generators           | 491 ms                                                                | 529 ms: 1.08x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 158 ms: 1.08x slower                                                     |
| thrift                     | 937 us                                                                | 1.02 ms: 1.08x slower                                                    |
| scimark_fft                | 418 ms                                                                | 455 ms: 1.09x slower                                                     |
| pyflate                    | 559 ms                                                                | 609 ms: 1.09x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 399 us: 1.09x slower                                                     |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.10x slower                                                     |
| nbody                      | 105 ms                                                                | 116 ms: 1.10x slower                                                     |
| regex_effbot               | 4.64 ms                                                               | 5.20 ms: 1.12x slower                                                    |
| fannkuch                   | 443 ms                                                                | 502 ms: 1.13x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 73.7 ms: 1.13x slower                                                    |
| generators                 | 43.5 ms                                                               | 49.3 ms: 1.13x slower                                                    |
| spectral_norm              | 131 ms                                                                | 150 ms: 1.15x slower                                                     |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.16x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.71 ms: 1.17x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.14 ms: 1.17x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.98 ms: 1.17x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.30 ms: 1.18x slower                                                    |
| go                         | 157 ms                                                                | 185 ms: 1.18x slower                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 19.7 ms: 1.18x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 33.6 ms: 1.18x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                    |
| chaos                      | 71.4 ms                                                               | 87.3 ms: 1.22x slower                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 193 ms: 1.22x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 33.6 ms: 1.23x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.55 sec: 1.23x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 123 ms: 1.24x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 225 us: 1.25x slower                                                     |
| richards_super             | 58.5 ms                                                               | 73.8 ms: 1.26x slower                                                    |
| richards                   | 50.9 ms                                                               | 64.4 ms: 1.27x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.79 sec: 1.27x slower                                                   |
| sympy_str                  | 280 ms                                                                | 356 ms: 1.27x slower                                                     |
| django_template            | 40.7 ms                                                               | 52.5 ms: 1.29x slower                                                    |
| 2to3                       | 308 ms                                                                | 398 ms: 1.29x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 164 ms: 1.30x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 80.9 ms: 1.30x slower                                                    |
| regex_compile              | 137 ms                                                                | 180 ms: 1.31x slower                                                     |
| sympy_expand               | 454 ms                                                                | 596 ms: 1.31x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 29.4 ms: 1.36x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 212 ms: 1.37x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.26 sec: 1.37x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 84.7 ms: 1.38x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 84.6 ms: 1.40x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.66 sec: 1.41x slower                                                   |
| pylint                     | 355 ms                                                                | 502 ms: 1.42x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.1 ms: 1.45x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.43 ms: 1.46x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.83 ms: 1.99x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.37 sec: 336.26x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.19x slower                                                             |

Benchmark hidden because not significant (10): comprehensions, xml_etree_iterparse, logging_format, xml_etree_parse, logging_simple, regex_dna, xml_etree_generate, deepcopy_reduce, coroutines, pidigits
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241113-3.14.0a1+-c695e37-JIT/bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37.json: bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.087x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x