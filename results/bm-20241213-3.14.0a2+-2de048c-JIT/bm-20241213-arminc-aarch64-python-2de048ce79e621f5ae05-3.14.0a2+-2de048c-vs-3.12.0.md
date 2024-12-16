# Results vs. 3.12.0

- fork: python
- ref: 2de048ce79e621f5ae05
- machine: linux-aarch64
- commit hash: 2de048c
- commit date: 2024-12-13
- overall geometric mean: 1.027x slower
- HPT reliability: 97.91%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 318 ms: 1.03x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.20 sec: 1.07x slower                                                   |
| html5lib       | 65.1 ms                                                               | 70.9 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 909 ms: 1.55x faster                                                     |
| async_tree_none            | 624 ms                                                                | 406 ms: 1.54x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 509 ms: 1.53x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 488 ms: 1.52x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 945 ms: 1.49x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 398 ms: 1.45x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 699 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 682 ms: 1.30x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.46x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 242 ms: 1.04x slower                                                     |
| nbody          | 105 ms                                                                | 117 ms: 1.12x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.05 ms: 1.15x faster                                                    |
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 32.1 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 179 ms: 1.09x faster                                                     |
| xml_etree_iterparse | 150 ms                                                                | 144 ms: 1.05x faster                                                     |
| tomli_loads         | 2.59 sec                                                              | 2.51 sec: 1.03x faster                                                   |
| json_loads          | 30.7 us                                                               | 32.4 us: 1.06x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 415 us: 1.14x slower                                                     |
| json_dumps          | 12.3 ms                                                               | 14.9 ms: 1.22x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_generate, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.07 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.3 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.5 ms: 1.05x slower                                                    |
| django_template | 40.7 ms                                                               | 48.0 ms: 1.18x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 32.4 ms: 1.18x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 80.3 ms: 1.33x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.18x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 909 ms: 1.55x faster                                                     |
| async_tree_none            | 624 ms                                                                | 406 ms: 1.54x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 509 ms: 1.53x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 488 ms: 1.52x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 945 ms: 1.49x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 398 ms: 1.45x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 699 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 682 ms: 1.30x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 41.6 us: 1.19x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.05 ms: 1.15x faster                                                    |
| deepcopy                   | 446 us                                                                | 399 us: 1.12x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 23.1 ms: 1.06x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.05x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.51 sec: 1.03x faster                                                   |
| comprehensions             | 25.4 us                                                               | 24.7 us: 1.03x faster                                                    |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.9 ms: 1.03x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 16.3 ms: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.6 ms: 1.02x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 158 ms: 1.03x slower                                                     |
| 2to3                       | 308 ms                                                                | 318 ms: 1.03x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 4.27 ms: 1.04x slower                                                    |
| logging_format             | 8.34 us                                                               | 8.67 us: 1.04x slower                                                    |
| pidigits                   | 233 ms                                                                | 242 ms: 1.04x slower                                                     |
| logging_simple             | 7.63 us                                                               | 7.96 us: 1.04x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.56 sec: 1.04x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.91 ms: 1.05x slower                                                    |
| raytrace                   | 353 ms                                                                | 370 ms: 1.05x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.5 ms: 1.05x slower                                                    |
| json                       | 5.54 ms                                                               | 5.82 ms: 1.05x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.4 us: 1.06x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.39 ms: 1.06x slower                                                    |
| spectral_norm              | 131 ms                                                                | 139 ms: 1.06x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.60 ms: 1.07x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 155 ms: 1.07x slower                                                     |
| sympy_str                  | 280 ms                                                                | 299 ms: 1.07x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.20 sec: 1.07x slower                                                   |
| thrift                     | 937 us                                                                | 1.01 ms: 1.07x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 23.3 ms: 1.08x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.07 ms: 1.08x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 93.9 ms: 1.08x slower                                                    |
| async_generators           | 491 ms                                                                | 532 ms: 1.08x slower                                                     |
| go                         | 157 ms                                                                | 171 ms: 1.09x slower                                                     |
| scimark_sor                | 150 ms                                                                | 163 ms: 1.09x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 4.11 us: 1.09x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 70.9 ms: 1.09x slower                                                    |
| pyflate                    | 559 ms                                                                | 609 ms: 1.09x slower                                                     |
| richards_super             | 58.5 ms                                                               | 64.6 ms: 1.11x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 139 ms: 1.11x slower                                                     |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.11x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.63 ms: 1.11x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 68.4 ms: 1.12x slower                                                    |
| nbody                      | 105 ms                                                                | 117 ms: 1.12x slower                                                     |
| sympy_expand               | 454 ms                                                                | 511 ms: 1.13x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 69.9 ms: 1.13x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 32.1 ms: 1.13x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 415 us: 1.14x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.43 sec: 1.14x slower                                                   |
| fannkuch                   | 443 ms                                                                | 506 ms: 1.14x slower                                                     |
| logging_silent             | 127 ns                                                                | 147 ns: 1.16x slower                                                     |
| richards                   | 50.9 ms                                                               | 59.3 ms: 1.16x slower                                                    |
| generators                 | 43.5 ms                                                               | 50.7 ms: 1.16x slower                                                    |
| django_template            | 40.7 ms                                                               | 48.0 ms: 1.18x slower                                                    |
| telco                      | 8.51 ms                                                               | 10.0 ms: 1.18x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 32.4 ms: 1.18x slower                                                    |
| chaos                      | 71.4 ms                                                               | 85.9 ms: 1.20x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.9 ms: 1.22x slower                                                    |
| coverage                   | 87.3 ms                                                               | 107 ms: 1.23x slower                                                     |
| mypy2                      | 873 ms                                                                | 1.08 sec: 1.23x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 226 us: 1.25x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 130 ms: 1.31x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 80.3 ms: 1.33x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 9.31 ms: 1.33x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.27 sec: 1.39x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.62 sec: 1.39x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.3 ms: 1.43x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.94 ms: 1.58x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.66 ms: 1.91x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.66 sec: 235.26x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.11x slower                                                             |

Benchmark hidden because not significant (10): pylint, sqlalchemy_declarative, xml_etree_generate, scimark_fft, float, deepcopy_reduce, asyncio_websockets, unpickle_pure_python, xml_etree_process, regex_compile
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241213-3.14.0a2+-2de048c-JIT/bm-20241213-arminc-aarch64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.027x slower

# HPT report

- Reliability score: 97.91% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x