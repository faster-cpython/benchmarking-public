# Results vs. 3.12.0

- fork: eendebakpt
- ref: 05f479c7b36947e5f3e9
- machine: darwin-arm64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.117x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 160 ms: 1.06x faster                                                       |
| docutils       | 1.50 sec                                               | 1.38 sec: 1.09x faster                                                     |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 360 ms: 1.86x faster                                                       |
| async_tree_io              | 668 ms                                                 | 363 ms: 1.84x faster                                                       |
| async_tree_none_tg         | 258 ms                                                 | 147 ms: 1.76x faster                                                       |
| async_tree_memoization_tg  | 323 ms                                                 | 190 ms: 1.70x faster                                                       |
| async_tree_none            | 266 ms                                                 | 158 ms: 1.68x faster                                                       |
| async_tree_memoization     | 312 ms                                                 | 199 ms: 1.57x faster                                                       |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 413 ms: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 414 ms: 1.27x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.60x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.9 ms: 1.19x faster                                                      |
| nbody          | 68.8 ms                                                | 67.5 ms: 1.02x faster                                                      |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.08 ms: 1.27x faster                                                      |
| regex_compile  | 77.9 ms                                                | 65.0 ms: 1.20x faster                                                      |
| regex_dna      | 154 ms                                                 | 137 ms: 1.13x faster                                                       |
| regex_v8       | 16.0 ms                                                | 16.0 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                               | 1.19 sec: 1.18x faster                                                     |
| unpickle_pure_python | 151 us                                                 | 136 us: 1.11x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                | 51.6 ms: 1.08x faster                                                      |
| xml_etree_process    | 39.7 ms                                                | 37.5 ms: 1.06x faster                                                      |
| json_loads           | 17.2 us                                                | 16.3 us: 1.06x faster                                                      |
| xml_etree_iterparse  | 74.0 ms                                                | 71.8 ms: 1.03x faster                                                      |
| xml_etree_parse      | 106 ms                                                 | 104 ms: 1.02x faster                                                       |
| pickle_pure_python   | 200 us                                                 | 196 us: 1.02x faster                                                       |
| json_dumps           | 6.22 ms                                                | 7.23 ms: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 12.3 ms: 1.31x slower                                                      |
| python_startup         | 11.4 ms                                                | 17.0 ms: 1.49x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.40x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 20.3 ms: 1.10x faster                                                      |
| mako            | 7.71 ms                                                | 7.13 ms: 1.08x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 360 ms: 1.86x faster                                                       |
| async_tree_io              | 668 ms                                                 | 363 ms: 1.84x faster                                                       |
| async_tree_none_tg         | 258 ms                                                 | 147 ms: 1.76x faster                                                       |
| async_tree_memoization_tg  | 323 ms                                                 | 190 ms: 1.70x faster                                                       |
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                       |
| async_tree_none            | 266 ms                                                 | 158 ms: 1.68x faster                                                       |
| deepcopy                   | 235 us                                                 | 146 us: 1.61x faster                                                       |
| async_tree_memoization     | 312 ms                                                 | 199 ms: 1.57x faster                                                       |
| deepcopy_memo              | 27.7 us                                                | 18.1 us: 1.53x faster                                                      |
| generators                 | 31.1 ms                                                | 22.5 ms: 1.38x faster                                                      |
| deepcopy_reduce            | 2.07 us                                                | 1.53 us: 1.35x faster                                                      |
| go                         | 102 ms                                                 | 77.1 ms: 1.32x faster                                                      |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 413 ms: 1.29x faster                                                       |
| regex_effbot               | 2.64 ms                                                | 2.08 ms: 1.27x faster                                                      |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 414 ms: 1.27x faster                                                       |
| raytrace                   | 212 ms                                                 | 168 ms: 1.26x faster                                                       |
| spectral_norm              | 76.4 ms                                                | 61.4 ms: 1.24x faster                                                      |
| comprehensions             | 14.5 us                                                | 12.1 us: 1.21x faster                                                      |
| regex_compile              | 77.9 ms                                                | 65.0 ms: 1.20x faster                                                      |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.20x faster                                                      |
| float                      | 55.8 ms                                                | 46.9 ms: 1.19x faster                                                      |
| deltablue                  | 2.71 ms                                                | 2.30 ms: 1.18x faster                                                      |
| logging_silent             | 76.4 ns                                                | 64.9 ns: 1.18x faster                                                      |
| logging_simple             | 3.69 us                                                | 3.13 us: 1.18x faster                                                      |
| tomli_loads                | 1.39 sec                                               | 1.19 sec: 1.18x faster                                                     |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.67 ms: 1.17x faster                                                      |
| logging_format             | 3.98 us                                                | 3.42 us: 1.16x faster                                                      |
| nqueens                    | 62.4 ms                                                | 54.4 ms: 1.15x faster                                                      |
| chaos                      | 42.5 ms                                                | 37.2 ms: 1.14x faster                                                      |
| scimark_fft                | 195 ms                                                 | 171 ms: 1.14x faster                                                       |
| regex_dna                  | 154 ms                                                 | 137 ms: 1.13x faster                                                       |
| sqlglot_transpile          | 1.02 ms                                                | 912 us: 1.12x faster                                                       |
| sqlglot_parse              | 848 us                                                 | 760 us: 1.12x faster                                                       |
| scimark_sor                | 87.4 ms                                                | 78.6 ms: 1.11x faster                                                      |
| pprint_pformat             | 1.01 sec                                               | 912 ms: 1.11x faster                                                       |
| unpickle_pure_python       | 151 us                                                 | 136 us: 1.11x faster                                                       |
| pathlib                    | 24.2 ms                                                | 22.0 ms: 1.10x faster                                                      |
| django_template            | 22.3 ms                                                | 20.3 ms: 1.10x faster                                                      |
| pprint_safe_repr           | 497 ms                                                 | 453 ms: 1.10x faster                                                       |
| async_generators           | 304 ms                                                 | 277 ms: 1.10x faster                                                       |
| dulwich_log                | 29.8 ms                                                | 27.2 ms: 1.10x faster                                                      |
| hexiom                     | 4.54 ms                                                | 4.15 ms: 1.09x faster                                                      |
| sqlglot_optimize           | 34.0 ms                                                | 31.1 ms: 1.09x faster                                                      |
| pyflate                    | 316 ms                                                 | 289 ms: 1.09x faster                                                       |
| sqlalchemy_declarative     | 62.3 ms                                                | 57.2 ms: 1.09x faster                                                      |
| sympy_str                  | 148 ms                                                 | 135 ms: 1.09x faster                                                       |
| sqlglot_normalize          | 186 ms                                                 | 171 ms: 1.09x faster                                                       |
| docutils                   | 1.50 sec                                               | 1.38 sec: 1.09x faster                                                     |
| xml_etree_generate         | 55.8 ms                                                | 51.6 ms: 1.08x faster                                                      |
| sympy_sum                  | 77.6 ms                                                | 71.7 ms: 1.08x faster                                                      |
| mako                       | 7.71 ms                                                | 7.13 ms: 1.08x faster                                                      |
| scimark_monte_carlo        | 45.0 ms                                                | 41.8 ms: 1.08x faster                                                      |
| bench_thread_pool          | 504 us                                                 | 468 us: 1.08x faster                                                       |
| json                       | 3.09 ms                                                | 2.87 ms: 1.08x faster                                                      |
| mdp                        | 1.58 sec                                               | 1.47 sec: 1.08x faster                                                     |
| pycparser                  | 677 ms                                                 | 631 ms: 1.07x faster                                                       |
| sympy_expand               | 241 ms                                                 | 226 ms: 1.06x faster                                                       |
| 2to3                       | 169 ms                                                 | 160 ms: 1.06x faster                                                       |
| xml_etree_process          | 39.7 ms                                                | 37.5 ms: 1.06x faster                                                      |
| json_loads                 | 17.2 us                                                | 16.3 us: 1.06x faster                                                      |
| sqlalchemy_imperative      | 6.68 ms                                                | 6.34 ms: 1.05x faster                                                      |
| sympy_integrate            | 11.4 ms                                                | 10.8 ms: 1.05x faster                                                      |
| scimark_lu                 | 76.0 ms                                                | 72.3 ms: 1.05x faster                                                      |
| xml_etree_iterparse        | 74.0 ms                                                | 71.8 ms: 1.03x faster                                                      |
| sqlite_synth               | 1.57 us                                                | 1.52 us: 1.03x faster                                                      |
| richards_super             | 36.0 ms                                                | 35.2 ms: 1.02x faster                                                      |
| xml_etree_parse            | 106 ms                                                 | 104 ms: 1.02x faster                                                       |
| nbody                      | 68.8 ms                                                | 67.5 ms: 1.02x faster                                                      |
| pickle_pure_python         | 200 us                                                 | 196 us: 1.02x faster                                                       |
| fannkuch                   | 248 ms                                                 | 245 ms: 1.02x faster                                                       |
| richards                   | 32.1 ms                                                | 31.7 ms: 1.01x faster                                                      |
| meteor_contest             | 71.7 ms                                                | 71.5 ms: 1.00x faster                                                      |
| regex_v8                   | 16.0 ms                                                | 16.0 ms: 1.00x slower                                                      |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                       |
| crypto_pyaes               | 51.9 ms                                                | 52.8 ms: 1.02x slower                                                      |
| json_dumps                 | 6.22 ms                                                | 7.23 ms: 1.16x slower                                                      |
| coverage                   | 38.9 ms                                                | 45.4 ms: 1.17x slower                                                      |
| telco                      | 3.68 ms                                                | 4.40 ms: 1.19x slower                                                      |
| gc_traversal               | 2.40 ms                                                | 3.09 ms: 1.29x slower                                                      |
| python_startup_no_site     | 9.37 ms                                                | 12.3 ms: 1.31x slower                                                      |
| bench_mp_pool              | 44.9 ms                                                | 59.1 ms: 1.32x slower                                                      |
| mypy2                      | 380 ms                                                 | 516 ms: 1.36x slower                                                       |
| python_startup             | 11.4 ms                                                | 17.0 ms: 1.49x slower                                                      |
| create_gc_cycles           | 701 us                                                 | 1.27 ms: 1.82x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                               |

Benchmark hidden because not significant (1): typing_runtime_protocols
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20250102-3.14.0a3+-05f479c/bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.117x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.20x