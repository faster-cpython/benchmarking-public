# Results vs. 3.12.0

- fork: python
- ref: 5cdd6e5e758a3fc0a5da
- machine: linux-aarch64
- commit hash: 5cdd6e5
- commit date: 2025-02-12
- overall geometric mean: 1.003x faster
- HPT reliability: 82.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 316 ms: 1.03x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.26 sec: 1.09x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 401 ms: 1.56x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 515 ms: 1.51x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 939 ms: 1.50x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 946 ms: 1.48x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 393 ms: 1.47x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 517 ms: 1.43x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 701 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 683 ms: 1.29x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.44x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.4 ms: 1.08x faster                                                    |
| pidigits       | 233 ms                                                                | 242 ms: 1.04x slower                                                     |
| nbody          | 105 ms                                                                | 129 ms: 1.23x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.91 ms: 1.19x faster                                                    |
| regex_compile  | 137 ms                                                                | 129 ms: 1.06x faster                                                     |
| regex_dna      | 254 ms                                                                | 244 ms: 1.04x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 32.0 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 179 ms: 1.09x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                   |
| unpickle_pure_python | 260 us                                                                | 274 us: 1.06x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 416 us: 1.14x slower                                                     |
| json_loads           | 30.7 us                                                               | 35.1 us: 1.14x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.7 ms: 1.02x faster                                                    |
| mako            | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 29.2 ms: 1.06x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 67.4 ms: 1.11x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.05x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 401 ms: 1.56x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 515 ms: 1.51x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 939 ms: 1.50x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 946 ms: 1.48x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 393 ms: 1.47x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 517 ms: 1.43x faster                                                     |
| deepcopy                   | 446 us                                                                | 342 us: 1.30x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 701 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 683 ms: 1.29x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 39.4 us: 1.26x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.6 ms: 1.19x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.91 ms: 1.19x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.50 us: 1.17x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.5 ms: 1.14x faster                                                    |
| spectral_norm              | 131 ms                                                                | 118 ms: 1.11x faster                                                     |
| pylint                     | 355 ms                                                                | 322 ms: 1.10x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                                     |
| float                      | 92.1 ms                                                               | 85.4 ms: 1.08x faster                                                    |
| regex_compile              | 137 ms                                                                | 129 ms: 1.06x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.88 us: 1.06x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.26 us: 1.05x faster                                                    |
| raytrace                   | 353 ms                                                                | 336 ms: 1.05x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 16.0 ms: 1.04x faster                                                    |
| regex_dna                  | 254 ms                                                                | 244 ms: 1.04x faster                                                     |
| chaos                      | 71.4 ms                                                               | 68.6 ms: 1.04x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 151 ms: 1.04x faster                                                     |
| scimark_lu                 | 146 ms                                                                | 140 ms: 1.04x faster                                                     |
| comprehensions             | 25.4 us                                                               | 24.6 us: 1.03x faster                                                    |
| django_template            | 40.7 ms                                                               | 39.7 ms: 1.02x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 152 ms: 1.02x faster                                                     |
| pyflate                    | 559 ms                                                                | 572 ms: 1.02x slower                                                     |
| 2to3                       | 308 ms                                                                | 316 ms: 1.03x slower                                                     |
| richards                   | 50.9 ms                                                               | 52.7 ms: 1.03x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.54 sec: 1.04x slower                                                   |
| pidigits                   | 233 ms                                                                | 242 ms: 1.04x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 1.91 ms: 1.04x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.97 us: 1.05x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 133 ms: 1.06x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 274 us: 1.06x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 22.9 ms: 1.06x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 29.2 ms: 1.06x slower                                                    |
| go                         | 157 ms                                                                | 169 ms: 1.07x slower                                                     |
| thrift                     | 937 us                                                                | 1.01 ms: 1.08x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.60 ms: 1.09x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.26 sec: 1.09x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 68.0 ms: 1.10x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 67.6 ms: 1.10x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.84 ms: 1.10x slower                                                    |
| json                       | 5.54 ms                                                               | 6.13 ms: 1.11x slower                                                    |
| logging_silent             | 127 ns                                                                | 140 ns: 1.11x slower                                                     |
| sympy_expand               | 454 ms                                                                | 504 ms: 1.11x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 67.4 ms: 1.11x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 32.0 ms: 1.13x slower                                                    |
| meteor_contest             | 112 ms                                                                | 127 ms: 1.13x slower                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 98.2 ms: 1.13x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 416 us: 1.14x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.43 sec: 1.14x slower                                                   |
| coverage                   | 87.3 ms                                                               | 99.7 ms: 1.14x slower                                                    |
| json_loads                 | 30.7 us                                                               | 35.1 us: 1.14x slower                                                    |
| telco                      | 8.51 ms                                                               | 10.1 ms: 1.19x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                    |
| fannkuch                   | 443 ms                                                                | 539 ms: 1.22x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 221 us: 1.22x slower                                                     |
| nbody                      | 105 ms                                                                | 129 ms: 1.23x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 127 ms: 1.28x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 9.00 ms: 1.29x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.35 sec: 1.47x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.78 sec: 1.47x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 7.12 ms: 1.62x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.63 ms: 1.89x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.59 sec: 367.51x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.09x slower                                                             |

Benchmark hidden because not significant (14): xml_etree_iterparse, async_generators, richards_super, xml_etree_generate, html5lib, coroutines, scimark_fft, scimark_monte_carlo, asyncio_websockets, scimark_sor, deltablue, sympy_str, bench_thread_pool, xml_etree_process
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250212-3.14.0a4+-5cdd6e5-JIT/bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 82.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x