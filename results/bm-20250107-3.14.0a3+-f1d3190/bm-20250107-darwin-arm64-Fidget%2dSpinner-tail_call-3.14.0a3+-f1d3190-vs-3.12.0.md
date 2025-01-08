# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: darwin-arm64
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.179x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 151 ms: 1.12x faster                                                  |
| docutils       | 1.50 sec                                               | 1.37 sec: 1.10x faster                                                |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 331 ms: 2.02x faster                                                  |
| async_tree_io              | 668 ms                                                 | 348 ms: 1.92x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 138 ms: 1.86x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 181 ms: 1.79x faster                                                  |
| async_tree_none            | 266 ms                                                 | 152 ms: 1.74x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 191 ms: 1.64x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 398 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 401 ms: 1.31x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.68x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 43.4 ms: 1.29x faster                                                 |
| nbody          | 68.8 ms                                                | 60.2 ms: 1.14x faster                                                 |
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.05 ms: 1.29x faster                                                 |
| regex_compile  | 77.9 ms                                                | 61.9 ms: 1.26x faster                                                 |
| regex_dna      | 154 ms                                                 | 138 ms: 1.12x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.8 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                 | 120 us: 1.25x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.14 sec: 1.22x faster                                                |
| xml_etree_process    | 39.7 ms                                                | 33.9 ms: 1.17x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 48.4 ms: 1.15x faster                                                 |
| pickle_pure_python   | 200 us                                                 | 182 us: 1.10x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 97.7 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 68.8 ms: 1.08x faster                                                 |
| json_loads           | 17.2 us                                                | 16.1 us: 1.07x faster                                                 |
| json_dumps           | 6.22 ms                                                | 7.08 ms: 1.14x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.6 ms: 1.45x slower                                                 |
| python_startup         | 11.4 ms                                                | 18.6 ms: 1.63x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.54x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.1 ms: 1.17x faster                                                 |
| mako            | 7.71 ms                                                | 6.91 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 331 ms: 2.02x faster                                                  |
| async_tree_io              | 668 ms                                                 | 348 ms: 1.92x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 138 ms: 1.86x faster                                                  |
| generators                 | 31.1 ms                                                | 17.2 ms: 1.81x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 181 ms: 1.79x faster                                                  |
| async_tree_none            | 266 ms                                                 | 152 ms: 1.74x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                  |
| deepcopy                   | 235 us                                                 | 140 us: 1.68x faster                                                  |
| deepcopy_memo              | 27.7 us                                                | 16.5 us: 1.67x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 191 ms: 1.64x faster                                                  |
| go                         | 102 ms                                                 | 70.9 ms: 1.43x faster                                                 |
| deepcopy_reduce            | 2.07 us                                                | 1.46 us: 1.42x faster                                                 |
| raytrace                   | 212 ms                                                 | 152 ms: 1.39x faster                                                  |
| comprehensions             | 14.5 us                                                | 10.7 us: 1.35x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 398 ms: 1.34x faster                                                  |
| logging_silent             | 76.4 ns                                                | 57.8 ns: 1.32x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.05 ms: 1.32x faster                                                 |
| coroutines                 | 19.2 ms                                                | 14.7 ms: 1.31x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 401 ms: 1.31x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 59.4 ms: 1.29x faster                                                 |
| float                      | 55.8 ms                                                | 43.4 ms: 1.29x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.05 ms: 1.29x faster                                                 |
| logging_simple             | 3.69 us                                                | 2.92 us: 1.26x faster                                                 |
| regex_compile              | 77.9 ms                                                | 61.9 ms: 1.26x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 120 us: 1.25x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 684 us: 1.24x faster                                                  |
| logging_format             | 3.98 us                                                | 3.23 us: 1.23x faster                                                 |
| chaos                      | 42.5 ms                                                | 34.5 ms: 1.23x faster                                                 |
| nqueens                    | 62.4 ms                                                | 50.7 ms: 1.23x faster                                                 |
| hexiom                     | 4.54 ms                                                | 3.71 ms: 1.22x faster                                                 |
| tomli_loads                | 1.39 sec                                               | 1.14 sec: 1.22x faster                                                |
| sqlglot_transpile          | 1.02 ms                                                | 840 us: 1.22x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.60 ms: 1.20x faster                                                 |
| scimark_sor                | 87.4 ms                                                | 72.7 ms: 1.20x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 37.6 ms: 1.20x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 64.6 ms: 1.18x faster                                                 |
| richards                   | 32.1 ms                                                | 27.4 ms: 1.17x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 33.9 ms: 1.17x faster                                                 |
| richards_super             | 36.0 ms                                                | 30.8 ms: 1.17x faster                                                 |
| django_template            | 22.3 ms                                                | 19.1 ms: 1.17x faster                                                 |
| scimark_fft                | 195 ms                                                 | 167 ms: 1.17x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 875 ms: 1.16x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 48.4 ms: 1.15x faster                                                 |
| nbody                      | 68.8 ms                                                | 60.2 ms: 1.14x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 437 ms: 1.14x faster                                                  |
| sympy_str                  | 148 ms                                                 | 130 ms: 1.14x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 26.2 ms: 1.14x faster                                                 |
| sqlalchemy_declarative     | 62.3 ms                                                | 55.3 ms: 1.13x faster                                                 |
| 2to3                       | 169 ms                                                 | 151 ms: 1.12x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 30.4 ms: 1.12x faster                                                 |
| sympy_sum                  | 77.6 ms                                                | 69.3 ms: 1.12x faster                                                 |
| sympy_integrate            | 11.4 ms                                                | 10.2 ms: 1.12x faster                                                 |
| pyflate                    | 316 ms                                                 | 282 ms: 1.12x faster                                                  |
| regex_dna                  | 154 ms                                                 | 138 ms: 1.12x faster                                                  |
| mako                       | 7.71 ms                                                | 6.91 ms: 1.12x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 167 ms: 1.11x faster                                                  |
| pycparser                  | 677 ms                                                 | 609 ms: 1.11x faster                                                  |
| crypto_pyaes               | 51.9 ms                                                | 46.6 ms: 1.11x faster                                                 |
| json                       | 3.09 ms                                                | 2.78 ms: 1.11x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 454 us: 1.11x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.43 sec: 1.11x faster                                                |
| docutils                   | 1.50 sec                                               | 1.37 sec: 1.10x faster                                                |
| sympy_expand               | 241 ms                                                 | 220 ms: 1.10x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 182 us: 1.10x faster                                                  |
| xml_etree_parse            | 106 ms                                                 | 97.7 ms: 1.09x faster                                                 |
| async_generators           | 304 ms                                                 | 279 ms: 1.09x faster                                                  |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.15 ms: 1.09x faster                                                 |
| pathlib                    | 24.2 ms                                                | 22.5 ms: 1.08x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 68.8 ms: 1.08x faster                                                 |
| json_loads                 | 17.2 us                                                | 16.1 us: 1.07x faster                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 89.7 us: 1.04x faster                                                 |
| fannkuch                   | 248 ms                                                 | 240 ms: 1.04x faster                                                  |
| meteor_contest             | 71.7 ms                                                | 70.0 ms: 1.03x faster                                                 |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                                 |
| pidigits                   | 282 ms                                                 | 280 ms: 1.01x faster                                                  |
| regex_v8                   | 16.0 ms                                                | 16.8 ms: 1.05x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 7.08 ms: 1.14x slower                                                 |
| coverage                   | 38.9 ms                                                | 45.0 ms: 1.16x slower                                                 |
| telco                      | 3.68 ms                                                | 4.41 ms: 1.20x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 3.06 ms: 1.28x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 59.9 ms: 1.33x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 13.6 ms: 1.45x slower                                                 |
| python_startup             | 11.4 ms                                                | 18.6 ms: 1.63x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 1.27 ms: 1.81x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                          |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20250107-3.14.0a3+-f1d3190/bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.179x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.18x