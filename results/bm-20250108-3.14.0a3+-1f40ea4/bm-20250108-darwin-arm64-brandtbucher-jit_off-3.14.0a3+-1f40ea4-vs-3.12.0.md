# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_off
- machine: darwin-arm64
- commit hash: 1f40ea4
- commit date: 2025-01-08
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 160 ms: 1.06x faster                                            |
| docutils       | 1.50 sec                                               | 1.40 sec: 1.07x faster                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 352 ms: 1.90x faster                                            |
| async_tree_io              | 668 ms                                                 | 365 ms: 1.83x faster                                            |
| async_tree_none_tg         | 258 ms                                                 | 148 ms: 1.74x faster                                            |
| async_tree_memoization_tg  | 323 ms                                                 | 186 ms: 1.73x faster                                            |
| async_tree_none            | 266 ms                                                 | 157 ms: 1.69x faster                                            |
| async_tree_memoization     | 312 ms                                                 | 197 ms: 1.59x faster                                            |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 407 ms: 1.31x faster                                            |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 415 ms: 1.27x faster                                            |
| Geometric mean             | (ref)                                                  | 1.62x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.4 ms: 1.20x faster                                           |
| pidigits       | 282 ms                                                 | 283 ms: 1.01x slower                                            |
| nbody          | 68.8 ms                                                | 70.0 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.05 ms: 1.29x faster                                           |
| regex_compile  | 77.9 ms                                                | 66.8 ms: 1.17x faster                                           |
| regex_dna      | 154 ms                                                 | 138 ms: 1.12x faster                                            |
| regex_v8       | 16.0 ms                                                | 15.8 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                  | 1.14x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                               | 1.19 sec: 1.17x faster                                          |
| unpickle_pure_python | 151 us                                                 | 137 us: 1.10x faster                                            |
| xml_etree_generate   | 55.8 ms                                                | 52.4 ms: 1.07x faster                                           |
| json_loads           | 17.2 us                                                | 16.5 us: 1.04x faster                                           |
| xml_etree_process    | 39.7 ms                                                | 38.0 ms: 1.04x faster                                           |
| xml_etree_iterparse  | 74.0 ms                                                | 71.6 ms: 1.03x faster                                           |
| xml_etree_parse      | 106 ms                                                 | 103 ms: 1.03x faster                                            |
| pickle_pure_python   | 200 us                                                 | 198 us: 1.01x faster                                            |
| json_dumps           | 6.22 ms                                                | 7.28 ms: 1.17x slower                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.8 ms: 1.48x slower                                           |
| python_startup         | 11.4 ms                                                | 18.8 ms: 1.65x slower                                           |
| Geometric mean         | (ref)                                                  | 1.56x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 20.9 ms: 1.07x faster                                           |
| mako            | 7.71 ms                                                | 7.24 ms: 1.07x faster                                           |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 352 ms: 1.90x faster                                            |
| async_tree_io              | 668 ms                                                 | 365 ms: 1.83x faster                                            |
| async_tree_none_tg         | 258 ms                                                 | 148 ms: 1.74x faster                                            |
| async_tree_memoization_tg  | 323 ms                                                 | 186 ms: 1.73x faster                                            |
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                            |
| async_tree_none            | 266 ms                                                 | 157 ms: 1.69x faster                                            |
| async_tree_memoization     | 312 ms                                                 | 197 ms: 1.59x faster                                            |
| deepcopy                   | 235 us                                                 | 149 us: 1.58x faster                                            |
| deepcopy_memo              | 27.7 us                                                | 17.9 us: 1.54x faster                                           |
| generators                 | 31.1 ms                                                | 22.3 ms: 1.39x faster                                           |
| deepcopy_reduce            | 2.07 us                                                | 1.56 us: 1.33x faster                                           |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 407 ms: 1.31x faster                                            |
| go                         | 102 ms                                                 | 78.3 ms: 1.30x faster                                           |
| regex_effbot               | 2.64 ms                                                | 2.05 ms: 1.29x faster                                           |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 415 ms: 1.27x faster                                            |
| raytrace                   | 212 ms                                                 | 168 ms: 1.26x faster                                            |
| spectral_norm              | 76.4 ms                                                | 61.6 ms: 1.24x faster                                           |
| coroutines                 | 19.2 ms                                                | 15.8 ms: 1.22x faster                                           |
| float                      | 55.8 ms                                                | 46.4 ms: 1.20x faster                                           |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.65 ms: 1.18x faster                                           |
| logging_silent             | 76.4 ns                                                | 65.0 ns: 1.18x faster                                           |
| tomli_loads                | 1.39 sec                                               | 1.19 sec: 1.17x faster                                          |
| comprehensions             | 14.5 us                                                | 12.4 us: 1.17x faster                                           |
| logging_simple             | 3.69 us                                                | 3.16 us: 1.17x faster                                           |
| regex_compile              | 77.9 ms                                                | 66.8 ms: 1.17x faster                                           |
| deltablue                  | 2.71 ms                                                | 2.34 ms: 1.16x faster                                           |
| logging_format             | 3.98 us                                                | 3.45 us: 1.15x faster                                           |
| scimark_fft                | 195 ms                                                 | 171 ms: 1.14x faster                                            |
| regex_dna                  | 154 ms                                                 | 138 ms: 1.12x faster                                            |
| chaos                      | 42.5 ms                                                | 38.0 ms: 1.12x faster                                           |
| sqlglot_parse              | 848 us                                                 | 759 us: 1.12x faster                                            |
| nqueens                    | 62.4 ms                                                | 56.2 ms: 1.11x faster                                           |
| scimark_sor                | 87.4 ms                                                | 78.6 ms: 1.11x faster                                           |
| dulwich_log                | 29.8 ms                                                | 26.9 ms: 1.11x faster                                           |
| pprint_pformat             | 1.01 sec                                               | 916 ms: 1.10x faster                                            |
| sqlglot_transpile          | 1.02 ms                                                | 926 us: 1.10x faster                                            |
| unpickle_pure_python       | 151 us                                                 | 137 us: 1.10x faster                                            |
| async_generators           | 304 ms                                                 | 277 ms: 1.10x faster                                            |
| hexiom                     | 4.54 ms                                                | 4.14 ms: 1.10x faster                                           |
| pprint_safe_repr           | 497 ms                                                 | 455 ms: 1.09x faster                                            |
| json                       | 3.09 ms                                                | 2.83 ms: 1.09x faster                                           |
| pyflate                    | 316 ms                                                 | 290 ms: 1.09x faster                                            |
| scimark_monte_carlo        | 45.0 ms                                                | 41.6 ms: 1.08x faster                                           |
| pathlib                    | 24.2 ms                                                | 22.4 ms: 1.08x faster                                           |
| docutils                   | 1.50 sec                                               | 1.40 sec: 1.07x faster                                          |
| sqlalchemy_declarative     | 62.3 ms                                                | 58.3 ms: 1.07x faster                                           |
| mdp                        | 1.58 sec                                               | 1.48 sec: 1.07x faster                                          |
| pycparser                  | 677 ms                                                 | 634 ms: 1.07x faster                                            |
| django_template            | 22.3 ms                                                | 20.9 ms: 1.07x faster                                           |
| sympy_str                  | 148 ms                                                 | 138 ms: 1.07x faster                                            |
| mako                       | 7.71 ms                                                | 7.24 ms: 1.07x faster                                           |
| xml_etree_generate         | 55.8 ms                                                | 52.4 ms: 1.07x faster                                           |
| bench_thread_pool          | 504 us                                                 | 475 us: 1.06x faster                                            |
| 2to3                       | 169 ms                                                 | 160 ms: 1.06x faster                                            |
| sympy_sum                  | 77.6 ms                                                | 73.5 ms: 1.06x faster                                           |
| sqlglot_optimize           | 34.0 ms                                                | 32.5 ms: 1.05x faster                                           |
| scimark_lu                 | 76.0 ms                                                | 72.6 ms: 1.05x faster                                           |
| json_loads                 | 17.2 us                                                | 16.5 us: 1.04x faster                                           |
| xml_etree_process          | 39.7 ms                                                | 38.0 ms: 1.04x faster                                           |
| sqlglot_normalize          | 186 ms                                                 | 179 ms: 1.04x faster                                            |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.46 ms: 1.04x faster                                           |
| xml_etree_iterparse        | 74.0 ms                                                | 71.6 ms: 1.03x faster                                           |
| xml_etree_parse            | 106 ms                                                 | 103 ms: 1.03x faster                                            |
| sqlite_synth               | 1.57 us                                                | 1.52 us: 1.03x faster                                           |
| sympy_expand               | 241 ms                                                 | 234 ms: 1.03x faster                                            |
| sympy_integrate            | 11.4 ms                                                | 11.1 ms: 1.02x faster                                           |
| richards_super             | 36.0 ms                                                | 35.3 ms: 1.02x faster                                           |
| richards                   | 32.1 ms                                                | 31.6 ms: 1.02x faster                                           |
| regex_v8                   | 16.0 ms                                                | 15.8 ms: 1.01x faster                                           |
| pickle_pure_python         | 200 us                                                 | 198 us: 1.01x faster                                            |
| meteor_contest             | 71.7 ms                                                | 71.1 ms: 1.01x faster                                           |
| pidigits                   | 282 ms                                                 | 283 ms: 1.01x slower                                            |
| nbody                      | 68.8 ms                                                | 70.0 ms: 1.02x slower                                           |
| crypto_pyaes               | 51.9 ms                                                | 52.8 ms: 1.02x slower                                           |
| typing_runtime_protocols   | 93.0 us                                                | 95.8 us: 1.03x slower                                           |
| json_dumps                 | 6.22 ms                                                | 7.28 ms: 1.17x slower                                           |
| coverage                   | 38.9 ms                                                | 45.9 ms: 1.18x slower                                           |
| telco                      | 3.68 ms                                                | 4.55 ms: 1.24x slower                                           |
| gc_traversal               | 2.40 ms                                                | 3.16 ms: 1.32x slower                                           |
| bench_mp_pool              | 44.9 ms                                                | 60.6 ms: 1.35x slower                                           |
| python_startup_no_site     | 9.37 ms                                                | 13.8 ms: 1.48x slower                                           |
| python_startup             | 11.4 ms                                                | 18.8 ms: 1.65x slower                                           |
| create_gc_cycles           | 701 us                                                 | 1.28 ms: 1.82x slower                                           |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                    |

Benchmark hidden because not significant (1): fannkuch
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20250108-3.14.0a3+-1f40ea4/bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.111x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.18x