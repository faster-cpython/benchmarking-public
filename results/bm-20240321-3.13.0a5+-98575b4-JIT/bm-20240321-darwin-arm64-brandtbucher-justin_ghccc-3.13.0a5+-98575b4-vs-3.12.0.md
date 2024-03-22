# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_ghccc
- machine: darwin-arm64
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.26x slower
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.43x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 192 ms: 1.14x slower                                                 |
| chameleon      | 4.70 ms                                                | 4.48 ms: 1.05x faster                                                |
| docutils       | 1.50 sec                                               | 2.61 sec: 1.74x slower                                               |
| tornado_http   | 69.3 ms                                                | 78.3 ms: 1.13x slower                                                |
| Geometric mean | (ref)                                                  | 1.21x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 526 ms                                                 | 2.81 sec: 5.34x slower                                               |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 2.96 sec: 5.55x slower                                               |
| async_tree_none            | 266 ms                                                 | 2.21 sec: 8.31x slower                                               |
| async_tree_memoization     | 312 ms                                                 | 2.83 sec: 9.06x slower                                               |
| async_tree_memoization_tg  | 323 ms                                                 | 2.97 sec: 9.20x slower                                               |
| async_tree_none_tg         | 258 ms                                                 | 2.44 sec: 9.48x slower                                               |
| async_tree_io              | 668 ms                                                 | 8.95 sec: 13.39x slower                                              |
| async_tree_io_tg           | 669 ms                                                 | 9.42 sec: 14.08x slower                                              |
| Geometric mean             | (ref)                                                  | 8.82x slower                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                 |
| nbody          | 68.8 ms                                                | 72.4 ms: 1.05x slower                                                |
| float          | 55.8 ms                                                | 89.7 ms: 1.61x slower                                                |
| Geometric mean | (ref)                                                  | 1.19x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 152 ms: 1.02x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.62 ms: 1.01x faster                                                |
| regex_compile  | 77.9 ms                                                | 83.2 ms: 1.07x slower                                                |
| regex_v8       | 16.0 ms                                                | 17.2 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 185 us: 1.08x faster                                                 |
| tomli_loads          | 1.39 sec                                               | 1.30 sec: 1.07x faster                                               |
| unpickle_pure_python | 151 us                                                 | 143 us: 1.05x faster                                                 |
| json_loads           | 17.2 us                                                | 17.1 us: 1.01x faster                                                |
| unpickle_list        | 3.02 us                                                | 3.08 us: 1.02x slower                                                |
| unpickle             | 9.12 us                                                | 9.33 us: 1.02x slower                                                |
| pickle               | 7.23 us                                                | 7.41 us: 1.03x slower                                                |
| json_dumps           | 6.22 ms                                                | 6.39 ms: 1.03x slower                                                |
| xml_etree_process    | 39.7 ms                                                | 41.3 ms: 1.04x slower                                                |
| pickle_list          | 2.89 us                                                | 3.01 us: 1.04x slower                                                |
| xml_etree_generate   | 55.8 ms                                                | 61.0 ms: 1.09x slower                                                |
| xml_etree_parse      | 106 ms                                                 | 131 ms: 1.23x slower                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 105 ms: 1.42x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x slower                                                         |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 18.9 ms: 1.66x slower                                                |
| python_startup_no_site | 9.37 ms                                                | 17.2 ms: 1.84x slower                                                |
| Geometric mean         | (ref)                                                  | 1.74x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.91 ms: 1.12x faster                                                |
| django_template | 22.3 ms                                                | 20.4 ms: 1.09x faster                                                |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols   | 93.0 us                                                | 69.6 us: 1.34x faster                                                |
| comprehensions             | 14.5 us                                                | 12.3 us: 1.18x faster                                                |
| logging_silent             | 76.4 ns                                                | 65.6 ns: 1.17x faster                                                |
| raytrace                   | 212 ms                                                 | 186 ms: 1.14x faster                                                 |
| generators                 | 31.1 ms                                                | 27.3 ms: 1.14x faster                                                |
| deepcopy_memo              | 27.7 us                                                | 24.4 us: 1.13x faster                                                |
| logging_simple             | 3.69 us                                                | 3.30 us: 1.12x faster                                                |
| mako                       | 7.71 ms                                                | 6.91 ms: 1.12x faster                                                |
| logging_format             | 3.98 us                                                | 3.58 us: 1.11x faster                                                |
| chaos                      | 42.5 ms                                                | 38.3 ms: 1.11x faster                                                |
| deepcopy_reduce            | 2.07 us                                                | 1.88 us: 1.10x faster                                                |
| crypto_pyaes               | 51.9 ms                                                | 47.1 ms: 1.10x faster                                                |
| deltablue                  | 2.71 ms                                                | 2.46 ms: 1.10x faster                                                |
| asyncio_tcp                | 449 ms                                                 | 409 ms: 1.10x faster                                                 |
| django_template            | 22.3 ms                                                | 20.4 ms: 1.09x faster                                                |
| pickle_pure_python         | 200 us                                                 | 185 us: 1.08x faster                                                 |
| deepcopy                   | 235 us                                                 | 217 us: 1.08x faster                                                 |
| tomli_loads                | 1.39 sec                                               | 1.30 sec: 1.07x faster                                               |
| coroutines                 | 19.2 ms                                                | 18.0 ms: 1.07x faster                                                |
| sympy_str                  | 148 ms                                                 | 138 ms: 1.07x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 174 ms: 1.06x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 143 us: 1.05x faster                                                 |
| chameleon                  | 4.70 ms                                                | 4.48 ms: 1.05x faster                                                |
| sympy_sum                  | 77.6 ms                                                | 74.5 ms: 1.04x faster                                                |
| json                       | 3.09 ms                                                | 2.96 ms: 1.04x faster                                                |
| sympy_integrate            | 11.4 ms                                                | 11.0 ms: 1.04x faster                                                |
| richards_super             | 36.0 ms                                                | 34.8 ms: 1.04x faster                                                |
| sqlglot_parse              | 848 us                                                 | 820 us: 1.03x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 493 us: 1.02x faster                                                 |
| regex_dna                  | 154 ms                                                 | 152 ms: 1.02x faster                                                 |
| sympy_expand               | 241 ms                                                 | 238 ms: 1.02x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.01 ms: 1.01x faster                                                |
| nqueens                    | 62.4 ms                                                | 61.6 ms: 1.01x faster                                                |
| richards                   | 32.1 ms                                                | 31.8 ms: 1.01x faster                                                |
| json_loads                 | 17.2 us                                                | 17.1 us: 1.01x faster                                                |
| regex_effbot               | 2.64 ms                                                | 2.62 ms: 1.01x faster                                                |
| dulwich_log                | 29.8 ms                                                | 29.8 ms: 1.00x faster                                                |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 496 ms: 1.00x faster                                                 |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.16 ms: 1.01x slower                                                |
| pprint_pformat             | 1.01 sec                                               | 1.02 sec: 1.01x slower                                               |
| gc_traversal               | 2.40 ms                                                | 2.44 ms: 1.02x slower                                                |
| sqlite_synth               | 1.57 us                                                | 1.60 us: 1.02x slower                                                |
| mdp                        | 1.58 sec                                               | 1.61 sec: 1.02x slower                                               |
| scimark_fft                | 195 ms                                                 | 199 ms: 1.02x slower                                                 |
| unpickle_list              | 3.02 us                                                | 3.08 us: 1.02x slower                                                |
| sqlglot_optimize           | 34.0 ms                                                | 34.7 ms: 1.02x slower                                                |
| pathlib                    | 24.2 ms                                                | 24.8 ms: 1.02x slower                                                |
| unpickle                   | 9.12 us                                                | 9.33 us: 1.02x slower                                                |
| pickle                     | 7.23 us                                                | 7.41 us: 1.03x slower                                                |
| json_dumps                 | 6.22 ms                                                | 6.39 ms: 1.03x slower                                                |
| go                         | 102 ms                                                 | 105 ms: 1.04x slower                                                 |
| xml_etree_process          | 39.7 ms                                                | 41.3 ms: 1.04x slower                                                |
| pickle_list                | 2.89 us                                                | 3.01 us: 1.04x slower                                                |
| meteor_contest             | 71.7 ms                                                | 75.0 ms: 1.05x slower                                                |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.31 sec: 1.05x slower                                               |
| nbody                      | 68.8 ms                                                | 72.4 ms: 1.05x slower                                                |
| gunicorn                   | 1.15 ms                                                | 1.22 ms: 1.07x slower                                                |
| pyflate                    | 316 ms                                                 | 336 ms: 1.07x slower                                                 |
| hexiom                     | 4.54 ms                                                | 4.85 ms: 1.07x slower                                                |
| regex_compile              | 77.9 ms                                                | 83.2 ms: 1.07x slower                                                |
| fannkuch                   | 248 ms                                                 | 266 ms: 1.07x slower                                                 |
| aiohttp                    | 1.08 ms                                                | 1.16 ms: 1.07x slower                                                |
| scimark_lu                 | 76.0 ms                                                | 81.5 ms: 1.07x slower                                                |
| regex_v8                   | 16.0 ms                                                | 17.2 ms: 1.08x slower                                                |
| create_gc_cycles           | 701 us                                                 | 760 us: 1.08x slower                                                 |
| xml_etree_generate         | 55.8 ms                                                | 61.0 ms: 1.09x slower                                                |
| tornado_http               | 69.3 ms                                                | 78.3 ms: 1.13x slower                                                |
| async_generators           | 304 ms                                                 | 345 ms: 1.13x slower                                                 |
| 2to3                       | 169 ms                                                 | 192 ms: 1.14x slower                                                 |
| coverage                   | 38.9 ms                                                | 46.8 ms: 1.20x slower                                                |
| scimark_sor                | 87.4 ms                                                | 106 ms: 1.22x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 54.8 ms: 1.22x slower                                                |
| xml_etree_parse            | 106 ms                                                 | 131 ms: 1.23x slower                                                 |
| pycparser                  | 677 ms                                                 | 834 ms: 1.23x slower                                                 |
| telco                      | 3.68 ms                                                | 4.54 ms: 1.23x slower                                                |
| mypy2                      | 380 ms                                                 | 533 ms: 1.40x slower                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 105 ms: 1.42x slower                                                 |
| float                      | 55.8 ms                                                | 89.7 ms: 1.61x slower                                                |
| python_startup             | 11.4 ms                                                | 18.9 ms: 1.66x slower                                                |
| docutils                   | 1.50 sec                                               | 2.61 sec: 1.74x slower                                               |
| python_startup_no_site     | 9.37 ms                                                | 17.2 ms: 1.84x slower                                                |
| dask                       | 222 ms                                                 | 453 ms: 2.04x slower                                                 |
| unpack_sequence            | 31.5 ns                                                | 113 ns: 3.59x slower                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 2.81 sec: 5.34x slower                                               |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 2.96 sec: 5.55x slower                                               |
| async_tree_none            | 266 ms                                                 | 2.21 sec: 8.31x slower                                               |
| async_tree_memoization     | 312 ms                                                 | 2.83 sec: 9.06x slower                                               |
| async_tree_memoization_tg  | 323 ms                                                 | 2.97 sec: 9.20x slower                                               |
| async_tree_none_tg         | 258 ms                                                 | 2.44 sec: 9.48x slower                                               |
| async_tree_io              | 668 ms                                                 | 8.95 sec: 13.39x slower                                              |
| async_tree_io_tg           | 669 ms                                                 | 9.42 sec: 14.08x slower                                              |
| Geometric mean             | (ref)                                                  | 1.26x slower                                                         |

Benchmark hidden because not significant (3): scimark_monte_carlo, pickle_dict, spectral_norm
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240321-3.13.0a5+-98575b4-JIT/bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 99.78% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.43x