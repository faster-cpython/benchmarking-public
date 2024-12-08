# Results vs. 3.12.0

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: linux-aarch64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.030x slower
- HPT reliability: 99.72%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 319 ms: 1.03x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.20 sec: 1.07x slower                                                   |
| html5lib       | 65.1 ms                                                               | 72.9 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io              | 1.41 sec                                                              | 946 ms: 1.49x faster                                                     |
| async_tree_none            | 624 ms                                                                | 423 ms: 1.48x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 956 ms: 1.47x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 547 ms: 1.42x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 535 ms: 1.38x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 423 ms: 1.36x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 719 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 714 ms: 1.24x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.39x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 105 ms                                                                | 118 ms: 1.13x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.10 ms: 1.13x faster                                                    |
| regex_dna      | 254 ms                                                                | 264 ms: 1.04x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 32.4 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 179 ms: 1.09x faster                                                     |
| xml_etree_iterparse | 150 ms                                                                | 144 ms: 1.04x faster                                                     |
| tomli_loads         | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                   |
| json_loads          | 30.7 us                                                               | 32.3 us: 1.05x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 408 us: 1.12x slower                                                     |
| json_dumps          | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_generate, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.18 ms: 1.10x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.26x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                    |
| django_template | 40.7 ms                                                               | 48.4 ms: 1.19x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 32.7 ms: 1.19x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 82.0 ms: 1.35x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.20x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io              | 1.41 sec                                                              | 946 ms: 1.49x faster                                                     |
| async_tree_none            | 624 ms                                                                | 423 ms: 1.48x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 956 ms: 1.47x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 547 ms: 1.42x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 535 ms: 1.38x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 423 ms: 1.36x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 719 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 714 ms: 1.24x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 40.1 us: 1.24x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.10 ms: 1.13x faster                                                    |
| deepcopy                   | 446 us                                                                | 396 us: 1.12x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.1 ms: 1.11x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 147 ms: 1.07x faster                                                     |
| pylint                     | 355 ms                                                                | 336 ms: 1.05x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.04x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 16.4 ms: 1.02x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 671 ms: 1.02x slower                                                     |
| 2to3                       | 308 ms                                                                | 319 ms: 1.03x slower                                                     |
| logging_simple             | 7.63 us                                                               | 7.90 us: 1.03x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 88.5 ms: 1.04x slower                                                    |
| regex_dna                  | 254 ms                                                                | 264 ms: 1.04x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.59 sec: 1.05x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                    |
| logging_format             | 8.34 us                                                               | 8.89 us: 1.07x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.03 us: 1.07x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.20 sec: 1.07x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 166 ms: 1.07x slower                                                     |
| async_generators           | 491 ms                                                                | 528 ms: 1.08x slower                                                     |
| scimark_fft                | 418 ms                                                                | 452 ms: 1.08x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                    |
| sympy_str                  | 280 ms                                                                | 304 ms: 1.09x slower                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 94.2 ms: 1.09x slower                                                    |
| pyflate                    | 559 ms                                                                | 610 ms: 1.09x slower                                                     |
| scimark_sor                | 150 ms                                                                | 164 ms: 1.09x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 2.00 ms: 1.10x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.18 ms: 1.10x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.39 sec: 1.11x slower                                                   |
| richards                   | 50.9 ms                                                               | 56.7 ms: 1.11x slower                                                    |
| thrift                     | 937 us                                                                | 1.04 ms: 1.11x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 24.1 ms: 1.11x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.63 ms: 1.12x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.50 ms: 1.12x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 408 us: 1.12x slower                                                     |
| meteor_contest             | 112 ms                                                                | 125 ms: 1.12x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 72.9 ms: 1.12x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 69.6 ms: 1.12x slower                                                    |
| nbody                      | 105 ms                                                                | 118 ms: 1.13x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 69.7 ms: 1.14x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                    |
| go                         | 157 ms                                                                | 180 ms: 1.14x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 32.4 ms: 1.14x slower                                                    |
| logging_silent             | 127 ns                                                                | 146 ns: 1.15x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.13 ms: 1.15x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 145 ms: 1.15x slower                                                     |
| sympy_expand               | 454 ms                                                                | 523 ms: 1.15x slower                                                     |
| fannkuch                   | 443 ms                                                                | 512 ms: 1.15x slower                                                     |
| generators                 | 43.5 ms                                                               | 50.5 ms: 1.16x slower                                                    |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                     |
| chaos                      | 71.4 ms                                                               | 84.1 ms: 1.18x slower                                                    |
| spectral_norm              | 131 ms                                                                | 154 ms: 1.18x slower                                                     |
| django_template            | 40.7 ms                                                               | 48.4 ms: 1.19x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 32.7 ms: 1.19x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 220 us: 1.22x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 9.35 ms: 1.34x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 134 ms: 1.35x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 82.0 ms: 1.35x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.27 sec: 1.39x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.63 sec: 1.40x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.74 ms: 1.53x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.23 ms: 1.69x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.46 sec: 206.39x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.12x slower                                                             |

Benchmark hidden because not significant (14): xml_etree_generate, deepcopy_reduce, comprehensions, deltablue, unpickle_pure_python, json, xml_etree_process, raytrace, richards_super, coroutines, float, pidigits, regex_compile, scimark_lu
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241207-3.14.0a2+-79b7cab-JIT/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.030x slower

# HPT report

- Reliability score: 99.72% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.05x