# Results vs. 3.12.0

- fork: brandtbucher
- ref: jump_backoff
- machine: linux-aarch64
- commit hash: 5dd5806
- commit date: 2024-11-13
- overall geometric mean: 1.066x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 336 ms: 1.09x slower                                                   |
| docutils       | 2.98 sec                                                              | 3.62 sec: 1.21x slower                                                 |
| html5lib       | 65.1 ms                                                               | 72.9 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.14x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 562 ms: 1.32x faster                                                   |
| async_tree_none            | 624 ms                                                                | 473 ms: 1.32x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 463 ms: 1.25x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 625 ms: 1.24x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.18x faster                                                 |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 760 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 788 ms: 1.16x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                                 |
| Geometric mean             | (ref)                                                                 | 1.21x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 238 ms: 1.02x slower                                                   |
| float          | 92.1 ms                                                               | 96.2 ms: 1.04x slower                                                  |
| nbody          | 105 ms                                                                | 121 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 265 ms: 1.04x slower                                                   |
| regex_effbot   | 4.64 ms                                                               | 5.05 ms: 1.09x slower                                                  |
| regex_v8       | 28.3 ms                                                               | 33.3 ms: 1.17x slower                                                  |
| regex_compile  | 137 ms                                                                | 162 ms: 1.18x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|--------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads        | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                 |
| json_loads         | 30.7 us                                                               | 32.6 us: 1.06x slower                                                  |
| pickle_pure_python | 365 us                                                                | 397 us: 1.09x slower                                                   |
| json_dumps         | 12.3 ms                                                               | 14.3 ms: 1.17x slower                                                  |
| Geometric mean     | (ref)                                                                 | 1.04x slower                                                           |

Benchmark hidden because not significant (5): unpickle_pure_python, xml_etree_generate, xml_etree_parse, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.93 ms: 1.07x slower                                                  |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.41x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                  |
| django_template | 40.7 ms                                                               | 50.1 ms: 1.23x slower                                                  |
| genshi_text     | 27.4 ms                                                               | 34.0 ms: 1.24x slower                                                  |
| genshi_xml      | 60.6 ms                                                               | 83.2 ms: 1.37x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.21x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 562 ms: 1.32x faster                                                   |
| async_tree_none            | 624 ms                                                                | 473 ms: 1.32x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 463 ms: 1.25x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 625 ms: 1.24x faster                                                   |
| deepcopy_memo              | 49.6 us                                                               | 41.4 us: 1.20x faster                                                  |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.18x faster                                                 |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 760 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 788 ms: 1.16x faster                                                   |
| deepcopy                   | 446 us                                                                | 400 us: 1.11x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                                 |
| pathlib                    | 24.5 ms                                                               | 22.7 ms: 1.08x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 4.02 us: 1.02x faster                                                  |
| coroutines                 | 29.0 ms                                                               | 28.4 ms: 1.02x faster                                                  |
| sqlalchemy_declarative     | 157 ms                                                                | 155 ms: 1.02x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                 |
| asyncio_websockets         | 658 ms                                                                | 673 ms: 1.02x slower                                                   |
| pidigits                   | 233 ms                                                                | 238 ms: 1.02x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                  |
| scimark_lu                 | 146 ms                                                                | 151 ms: 1.03x slower                                                   |
| regex_dna                  | 254 ms                                                                | 265 ms: 1.04x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 90.5 ms: 1.04x slower                                                  |
| float                      | 92.1 ms                                                               | 96.2 ms: 1.04x slower                                                  |
| deltablue                  | 4.12 ms                                                               | 4.31 ms: 1.05x slower                                                  |
| mdp                        | 3.41 sec                                                              | 3.60 sec: 1.06x slower                                                 |
| json                       | 5.54 ms                                                               | 5.86 ms: 1.06x slower                                                  |
| bench_thread_pool          | 1.31 ms                                                               | 1.39 ms: 1.06x slower                                                  |
| json_loads                 | 30.7 us                                                               | 32.6 us: 1.06x slower                                                  |
| python_startup_no_site     | 8.37 ms                                                               | 8.93 ms: 1.07x slower                                                  |
| scimark_fft                | 418 ms                                                                | 446 ms: 1.07x slower                                                   |
| richards_super             | 58.5 ms                                                               | 62.6 ms: 1.07x slower                                                  |
| logging_silent             | 127 ns                                                                | 136 ns: 1.07x slower                                                   |
| thrift                     | 937 us                                                                | 1.01 ms: 1.07x slower                                                  |
| sqlite_synth               | 3.77 us                                                               | 4.05 us: 1.08x slower                                                  |
| async_generators           | 491 ms                                                                | 531 ms: 1.08x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 92.4 ms: 1.09x slower                                                  |
| pickle_pure_python         | 365 us                                                                | 397 us: 1.09x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 5.05 ms: 1.09x slower                                                  |
| scimark_sor                | 150 ms                                                                | 163 ms: 1.09x slower                                                   |
| 2to3                       | 308 ms                                                                | 336 ms: 1.09x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.00 ms: 1.09x slower                                                  |
| sqlglot_parse              | 1.46 ms                                                               | 1.60 ms: 1.09x slower                                                  |
| sqlalchemy_imperative      | 16.7 ms                                                               | 18.5 ms: 1.11x slower                                                  |
| generators                 | 43.5 ms                                                               | 48.4 ms: 1.11x slower                                                  |
| richards                   | 50.9 ms                                                               | 56.8 ms: 1.12x slower                                                  |
| html5lib                   | 65.1 ms                                                               | 72.9 ms: 1.12x slower                                                  |
| sympy_sum                  | 154 ms                                                                | 174 ms: 1.13x slower                                                   |
| coverage                   | 87.3 ms                                                               | 99.0 ms: 1.13x slower                                                  |
| meteor_contest             | 112 ms                                                                | 128 ms: 1.14x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 24.8 ms: 1.15x slower                                                  |
| nbody                      | 105 ms                                                                | 121 ms: 1.15x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.3 ms: 1.17x slower                                                  |
| regex_v8                   | 28.3 ms                                                               | 33.3 ms: 1.17x slower                                                  |
| telco                      | 8.51 ms                                                               | 10.0 ms: 1.18x slower                                                  |
| spectral_norm              | 131 ms                                                                | 154 ms: 1.18x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.31 ms: 1.18x slower                                                  |
| fannkuch                   | 443 ms                                                                | 523 ms: 1.18x slower                                                   |
| regex_compile              | 137 ms                                                                | 162 ms: 1.18x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 72.4 ms: 1.18x slower                                                  |
| pylint                     | 355 ms                                                                | 419 ms: 1.18x slower                                                   |
| pyflate                    | 559 ms                                                                | 661 ms: 1.18x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 149 ms: 1.18x slower                                                   |
| chaos                      | 71.4 ms                                                               | 84.6 ms: 1.18x slower                                                  |
| sympy_str                  | 280 ms                                                                | 335 ms: 1.20x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.51 sec: 1.20x slower                                                 |
| docutils                   | 2.98 sec                                                              | 3.62 sec: 1.21x slower                                                 |
| go                         | 157 ms                                                                | 193 ms: 1.22x slower                                                   |
| django_template            | 40.7 ms                                                               | 50.1 ms: 1.23x slower                                                  |
| typing_runtime_protocols   | 181 us                                                                | 223 us: 1.24x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 34.0 ms: 1.24x slower                                                  |
| nqueens                    | 99.2 ms                                                               | 126 ms: 1.27x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 80.0 ms: 1.29x slower                                                  |
| sympy_expand               | 454 ms                                                                | 592 ms: 1.30x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.54 sec: 1.35x slower                                                 |
| pprint_safe_repr           | 916 ms                                                                | 1.24 sec: 1.35x slower                                                 |
| genshi_xml                 | 60.6 ms                                                               | 83.2 ms: 1.37x slower                                                  |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.41x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 10.1 ms: 1.44x slower                                                  |
| gc_traversal               | 4.40 ms                                                               | 6.43 ms: 1.46x slower                                                  |
| create_gc_cycles           | 1.92 ms                                                               | 3.68 ms: 1.92x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 2.11 sec: 299.49x slower                                               |
| Geometric mean             | (ref)                                                                 | 1.16x slower                                                           |

Benchmark hidden because not significant (9): comprehensions, unpickle_pure_python, xml_etree_generate, xml_etree_parse, logging_format, xml_etree_process, logging_simple, raytrace, xml_etree_iterparse
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20241113-3.14.0a1+-5dd5806-JIT/bm-20241113-arminc-aarch64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806.json: bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.066x slower
# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.05x