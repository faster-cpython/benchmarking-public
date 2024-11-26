# Results vs. 3.12.0

- fork: python
- ref: 09d6f5dc7824c74672ad
- machine: linux-aarch64
- commit hash: 09d6f5d
- commit date: 2024-11-07
- overall geometric mean: 1.083x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 402 ms: 1.31x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.78 sec: 1.27x slower                                                   |
| html5lib       | 65.1 ms                                                               | 72.9 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.23x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 560 ms: 1.32x faster                                                     |
| async_tree_none            | 624 ms                                                                | 475 ms: 1.31x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 624 ms: 1.25x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 463 ms: 1.24x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 763 ms: 1.20x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.18x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 768 ms: 1.15x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.27 sec: 1.11x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.22x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 95.6 ms: 1.04x slower                                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 263 ms: 1.04x slower                                                     |
| regex_effbot   | 4.64 ms                                                               | 5.01 ms: 1.08x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                                    |
| regex_compile  | 137 ms                                                                | 179 ms: 1.31x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.14x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_loads           | 30.7 us                                                               | 32.2 us: 1.05x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 274 us: 1.06x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 412 us: 1.13x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 15.0 ms: 1.22x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_iterparse, tomli_loads, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.04 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.42x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                    |
| django_template | 40.7 ms                                                               | 50.5 ms: 1.24x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 34.7 ms: 1.27x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 84.9 ms: 1.40x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.23x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 560 ms: 1.32x faster                                                     |
| async_tree_none            | 624 ms                                                                | 475 ms: 1.31x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 624 ms: 1.25x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 463 ms: 1.24x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 763 ms: 1.20x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 41.7 us: 1.19x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.19 sec: 1.18x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 768 ms: 1.15x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.27 sec: 1.11x faster                                                   |
| deepcopy                   | 446 us                                                                | 407 us: 1.09x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.6 ms: 1.09x faster                                                    |
| comprehensions             | 25.4 us                                                               | 24.4 us: 1.04x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                                     |
| regex_dna                  | 254 ms                                                                | 263 ms: 1.04x slower                                                     |
| float                      | 92.1 ms                                                               | 95.6 ms: 1.04x slower                                                    |
| json                       | 5.54 ms                                                               | 5.76 ms: 1.04x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.30 ms: 1.04x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.2 us: 1.05x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 153 ms: 1.05x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.38 ms: 1.05x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 274 us: 1.06x slower                                                     |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.06x slower                                                     |
| scimark_fft                | 418 ms                                                                | 443 ms: 1.06x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.62 sec: 1.06x slower                                                   |
| thrift                     | 937 us                                                                | 1.00 ms: 1.07x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 93.1 ms: 1.08x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 5.01 ms: 1.08x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.04 ms: 1.08x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 91.9 ms: 1.08x slower                                                    |
| async_generators           | 491 ms                                                                | 533 ms: 1.09x slower                                                     |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                     |
| pyflate                    | 559 ms                                                                | 612 ms: 1.09x slower                                                     |
| logging_silent             | 127 ns                                                                | 140 ns: 1.10x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 72.9 ms: 1.12x slower                                                    |
| fannkuch                   | 443 ms                                                                | 500 ms: 1.13x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 412 us: 1.13x slower                                                     |
| meteor_contest             | 112 ms                                                                | 127 ms: 1.14x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 4.29 us: 1.14x slower                                                    |
| coverage                   | 87.3 ms                                                               | 99.8 ms: 1.14x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                                    |
| generators                 | 43.5 ms                                                               | 50.4 ms: 1.16x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.71 ms: 1.17x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.94 ms: 1.17x slower                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 19.6 ms: 1.18x slower                                                    |
| chaos                      | 71.4 ms                                                               | 84.3 ms: 1.18x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.33 ms: 1.18x slower                                                    |
| spectral_norm              | 131 ms                                                                | 156 ms: 1.20x slower                                                     |
| go                         | 157 ms                                                                | 189 ms: 1.20x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 2.20 ms: 1.21x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.51 sec: 1.21x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 219 us: 1.21x slower                                                     |
| pylint                     | 355 ms                                                                | 433 ms: 1.22x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 15.0 ms: 1.22x slower                                                    |
| django_template            | 40.7 ms                                                               | 50.5 ms: 1.24x slower                                                    |
| richards                   | 50.9 ms                                                               | 63.5 ms: 1.25x slower                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 197 ms: 1.25x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 124 ms: 1.25x slower                                                     |
| richards_super             | 58.5 ms                                                               | 73.6 ms: 1.26x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 34.7 ms: 1.27x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.78 sec: 1.27x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 162 ms: 1.29x slower                                                     |
| sympy_str                  | 280 ms                                                                | 362 ms: 1.29x slower                                                     |
| regex_compile              | 137 ms                                                                | 179 ms: 1.31x slower                                                     |
| 2to3                       | 308 ms                                                                | 402 ms: 1.31x slower                                                     |
| sympy_expand               | 454 ms                                                                | 597 ms: 1.32x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 28.9 ms: 1.34x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 83.3 ms: 1.34x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.26 sec: 1.37x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 212 ms: 1.38x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 85.5 ms: 1.39x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 84.9 ms: 1.40x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.66 sec: 1.41x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 9.88 ms: 1.42x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.42x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.30 ms: 1.43x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.84 ms: 2.00x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.58 sec: 224.57x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.18x slower                                                             |

Benchmark hidden because not significant (11): xml_etree_parse, logging_simple, logging_format, xml_etree_iterparse, coroutines, deepcopy_reduce, tomli_loads, xml_etree_generate, raytrace, pidigits, xml_etree_process
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-arminc-aarch64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.083x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.09x