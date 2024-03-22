# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_ghccc
- machine: darwin-arm64
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.30x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.48x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 154 ms                                                 | 192 ms: 1.25x slower                                                 |
| chameleon      | 4.30 ms                                                | 4.48 ms: 1.04x slower                                                |
| docutils       | 1.43 sec                                               | 2.61 sec: 1.82x slower                                               |
| html5lib       | 33.0 ms                                                | 38.0 ms: 1.15x slower                                                |
| tornado_http   | 69.1 ms                                                | 78.3 ms: 1.13x slower                                                |
| Geometric mean | (ref)                                                  | 1.25x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 2.96 sec: 5.37x slower                                               |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 2.81 sec: 5.41x slower                                               |
| async_tree_none            | 282 ms                                                 | 2.21 sec: 7.84x slower                                               |
| async_tree_memoization     | 336 ms                                                 | 2.83 sec: 8.42x slower                                               |
| async_tree_memoization_tg  | 352 ms                                                 | 2.97 sec: 8.42x slower                                               |
| async_tree_none_tg         | 276 ms                                                 | 2.44 sec: 8.84x slower                                               |
| async_tree_io              | 697 ms                                                 | 8.95 sec: 12.83x slower                                              |
| async_tree_io_tg           | 724 ms                                                 | 9.42 sec: 13.02x slower                                              |
| Geometric mean             | (ref)                                                  | 8.36x slower                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                 |
| nbody          | 61.7 ms                                                | 72.4 ms: 1.17x slower                                                |
| float          | 50.8 ms                                                | 89.7 ms: 1.77x slower                                                |
| Geometric mean | (ref)                                                  | 1.28x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 148 ms                                                 | 152 ms: 1.03x slower                                                 |
| regex_effbot   | 2.43 ms                                                | 2.62 ms: 1.08x slower                                                |
| regex_v8       | 15.1 ms                                                | 17.2 ms: 1.14x slower                                                |
| regex_compile  | 72.8 ms                                                | 83.2 ms: 1.14x slower                                                |
| Geometric mean | (ref)                                                  | 1.09x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps           | 7.53 ms                                                | 6.39 ms: 1.18x faster                                                |
| unpickle_pure_python | 149 us                                                 | 143 us: 1.04x faster                                                 |
| pickle_pure_python   | 191 us                                                 | 185 us: 1.04x faster                                                 |
| tomli_loads          | 1.27 sec                                               | 1.30 sec: 1.02x slower                                               |
| pickle_dict          | 17.1 us                                                | 18.1 us: 1.06x slower                                                |
| pickle               | 6.98 us                                                | 7.41 us: 1.06x slower                                                |
| json_loads           | 15.3 us                                                | 17.1 us: 1.11x slower                                                |
| pickle_list          | 2.70 us                                                | 3.01 us: 1.12x slower                                                |
| unpickle             | 8.29 us                                                | 9.33 us: 1.13x slower                                                |
| unpickle_list        | 2.69 us                                                | 3.08 us: 1.15x slower                                                |
| xml_etree_process    | 33.6 ms                                                | 41.3 ms: 1.23x slower                                                |
| xml_etree_parse      | 100 ms                                                 | 131 ms: 1.30x slower                                                 |
| xml_etree_generate   | 45.8 ms                                                | 61.0 ms: 1.33x slower                                                |
| xml_etree_iterparse  | 68.3 ms                                                | 105 ms: 1.54x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                | 18.9 ms: 1.76x slower                                                |
| python_startup_no_site | 8.57 ms                                                | 17.2 ms: 2.01x slower                                                |
| Geometric mean         | (ref)                                                  | 1.88x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 7.93 ms                                                | 6.91 ms: 1.15x faster                                                |
| django_template | 20.1 ms                                                | 20.4 ms: 1.01x slower                                                |
| genshi_text     | 14.4 ms                                                | 14.8 ms: 1.03x slower                                                |
| genshi_xml      | 28.5 ms                                                | 35.4 ms: 1.24x slower                                                |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols   | 301 us                                                 | 69.6 us: 4.32x faster                                                |
| asyncio_tcp                | 643 ms                                                 | 409 ms: 1.57x faster                                                 |
| chaos                      | 47.4 ms                                                | 38.3 ms: 1.24x faster                                                |
| json_dumps                 | 7.53 ms                                                | 6.39 ms: 1.18x faster                                                |
| comprehensions             | 14.4 us                                                | 12.3 us: 1.18x faster                                                |
| mako                       | 7.93 ms                                                | 6.91 ms: 1.15x faster                                                |
| deltablue                  | 2.75 ms                                                | 2.46 ms: 1.12x faster                                                |
| generators                 | 30.3 ms                                                | 27.3 ms: 1.11x faster                                                |
| raytrace                   | 206 ms                                                 | 186 ms: 1.11x faster                                                 |
| sqlglot_parse              | 890 us                                                 | 820 us: 1.09x faster                                                 |
| sympy_sum                  | 80.2 ms                                                | 74.5 ms: 1.08x faster                                                |
| richards_super             | 37.3 ms                                                | 34.8 ms: 1.07x faster                                                |
| asyncio_tcp_ssl            | 1.40 sec                                               | 1.31 sec: 1.07x faster                                               |
| deepcopy_memo              | 25.7 us                                                | 24.4 us: 1.06x faster                                                |
| sqlglot_transpile          | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                |
| unpickle_pure_python       | 149 us                                                 | 143 us: 1.04x faster                                                 |
| sympy_str                  | 144 ms                                                 | 138 ms: 1.04x faster                                                 |
| pickle_pure_python         | 191 us                                                 | 185 us: 1.04x faster                                                 |
| logging_simple             | 3.41 us                                                | 3.30 us: 1.03x faster                                                |
| sympy_integrate            | 11.3 ms                                                | 11.0 ms: 1.03x faster                                                |
| logging_format             | 3.67 us                                                | 3.58 us: 1.03x faster                                                |
| logging_silent             | 66.5 ns                                                | 65.6 ns: 1.01x faster                                                |
| crypto_pyaes               | 47.5 ms                                                | 47.1 ms: 1.01x faster                                                |
| deepcopy                   | 215 us                                                 | 217 us: 1.01x slower                                                 |
| pidigits                   | 280 ms                                                 | 283 ms: 1.01x slower                                                 |
| django_template            | 20.1 ms                                                | 20.4 ms: 1.01x slower                                                |
| tomli_loads                | 1.27 sec                                               | 1.30 sec: 1.02x slower                                               |
| richards                   | 31.1 ms                                                | 31.8 ms: 1.02x slower                                                |
| gc_traversal               | 2.38 ms                                                | 2.44 ms: 1.02x slower                                                |
| regex_dna                  | 148 ms                                                 | 152 ms: 1.03x slower                                                 |
| genshi_text                | 14.4 ms                                                | 14.8 ms: 1.03x slower                                                |
| scimark_monte_carlo        | 43.5 ms                                                | 45.0 ms: 1.03x slower                                                |
| sympy_expand               | 229 ms                                                 | 238 ms: 1.04x slower                                                 |
| pprint_safe_repr           | 478 ms                                                 | 496 ms: 1.04x slower                                                 |
| dulwich_log                | 28.6 ms                                                | 29.8 ms: 1.04x slower                                                |
| chameleon                  | 4.30 ms                                                | 4.48 ms: 1.04x slower                                                |
| pprint_pformat             | 979 ms                                                 | 1.02 sec: 1.05x slower                                               |
| deepcopy_reduce            | 1.79 us                                                | 1.88 us: 1.05x slower                                                |
| coroutines                 | 17.2 ms                                                | 18.0 ms: 1.05x slower                                                |
| meteor_contest             | 71.1 ms                                                | 75.0 ms: 1.06x slower                                                |
| hexiom                     | 4.58 ms                                                | 4.85 ms: 1.06x slower                                                |
| pickle_dict                | 17.1 us                                                | 18.1 us: 1.06x slower                                                |
| bench_thread_pool          | 465 us                                                 | 493 us: 1.06x slower                                                 |
| pickle                     | 6.98 us                                                | 7.41 us: 1.06x slower                                                |
| thrift                     | 410 us                                                 | 437 us: 1.06x slower                                                 |
| coverage                   | 43.9 ms                                                | 46.8 ms: 1.07x slower                                                |
| pathlib                    | 23.2 ms                                                | 24.8 ms: 1.07x slower                                                |
| create_gc_cycles           | 711 us                                                 | 760 us: 1.07x slower                                                 |
| json                       | 2.75 ms                                                | 2.96 ms: 1.08x slower                                                |
| sqlglot_normalize          | 162 ms                                                 | 174 ms: 1.08x slower                                                 |
| regex_effbot               | 2.43 ms                                                | 2.62 ms: 1.08x slower                                                |
| mdp                        | 1.48 sec                                               | 1.61 sec: 1.08x slower                                               |
| nqueens                    | 55.9 ms                                                | 61.6 ms: 1.10x slower                                                |
| fannkuch                   | 240 ms                                                 | 266 ms: 1.11x slower                                                 |
| json_loads                 | 15.3 us                                                | 17.1 us: 1.11x slower                                                |
| gunicorn                   | 1.10 ms                                                | 1.22 ms: 1.12x slower                                                |
| pickle_list                | 2.70 us                                                | 3.01 us: 1.12x slower                                                |
| scimark_sparse_mat_mult    | 2.81 ms                                                | 3.16 ms: 1.12x slower                                                |
| unpickle                   | 8.29 us                                                | 9.33 us: 1.13x slower                                                |
| aiohttp                    | 1.02 ms                                                | 1.16 ms: 1.13x slower                                                |
| tornado_http               | 69.1 ms                                                | 78.3 ms: 1.13x slower                                                |
| regex_v8                   | 15.1 ms                                                | 17.2 ms: 1.14x slower                                                |
| regex_compile              | 72.8 ms                                                | 83.2 ms: 1.14x slower                                                |
| unpickle_list              | 2.69 us                                                | 3.08 us: 1.15x slower                                                |
| scimark_fft                | 173 ms                                                 | 199 ms: 1.15x slower                                                 |
| html5lib                   | 33.0 ms                                                | 38.0 ms: 1.15x slower                                                |
| sqlglot_optimize           | 29.6 ms                                                | 34.7 ms: 1.17x slower                                                |
| nbody                      | 61.7 ms                                                | 72.4 ms: 1.17x slower                                                |
| pyflate                    | 284 ms                                                 | 336 ms: 1.19x slower                                                 |
| scimark_lu                 | 67.7 ms                                                | 81.5 ms: 1.20x slower                                                |
| spectral_norm              | 65.7 ms                                                | 79.8 ms: 1.21x slower                                                |
| xml_etree_process          | 33.6 ms                                                | 41.3 ms: 1.23x slower                                                |
| genshi_xml                 | 28.5 ms                                                | 35.4 ms: 1.24x slower                                                |
| 2to3                       | 154 ms                                                 | 192 ms: 1.25x slower                                                 |
| pycparser                  | 659 ms                                                 | 834 ms: 1.26x slower                                                 |
| sqlite_synth               | 1.26 us                                                | 1.60 us: 1.27x slower                                                |
| xml_etree_parse            | 100 ms                                                 | 131 ms: 1.30x slower                                                 |
| xml_etree_generate         | 45.8 ms                                                | 61.0 ms: 1.33x slower                                                |
| bench_mp_pool              | 41.0 ms                                                | 54.8 ms: 1.34x slower                                                |
| scimark_sor                | 79.2 ms                                                | 106 ms: 1.34x slower                                                 |
| mypy2                      | 372 ms                                                 | 533 ms: 1.43x slower                                                 |
| telco                      | 3.17 ms                                                | 4.54 ms: 1.43x slower                                                |
| xml_etree_iterparse        | 68.3 ms                                                | 105 ms: 1.54x slower                                                 |
| python_startup             | 10.8 ms                                                | 18.9 ms: 1.76x slower                                                |
| float                      | 50.8 ms                                                | 89.7 ms: 1.77x slower                                                |
| async_generators           | 192 ms                                                 | 345 ms: 1.79x slower                                                 |
| docutils                   | 1.43 sec                                               | 2.61 sec: 1.82x slower                                               |
| python_startup_no_site     | 8.57 ms                                                | 17.2 ms: 2.01x slower                                                |
| dask                       | 219 ms                                                 | 453 ms: 2.07x slower                                                 |
| pylint                     | 253 ms                                                 | 587 ms: 2.32x slower                                                 |
| unpack_sequence            | 33.6 ns                                                | 113 ns: 3.36x slower                                                 |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 2.96 sec: 5.37x slower                                               |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 2.81 sec: 5.41x slower                                               |
| async_tree_none            | 282 ms                                                 | 2.21 sec: 7.84x slower                                               |
| async_tree_memoization     | 336 ms                                                 | 2.83 sec: 8.42x slower                                               |
| async_tree_memoization_tg  | 352 ms                                                 | 2.97 sec: 8.42x slower                                               |
| async_tree_none_tg         | 276 ms                                                 | 2.44 sec: 8.84x slower                                               |
| async_tree_io              | 697 ms                                                 | 8.95 sec: 12.83x slower                                              |
| async_tree_io_tg           | 724 ms                                                 | 9.42 sec: 13.02x slower                                              |
| Geometric mean             | (ref)                                                  | 1.30x slower                                                         |

Benchmark hidden because not significant (2): go, asyncio_websockets
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (8) of results/bm-20240321-3.13.0a5+-98575b4-JIT/bm-20240321-darwin-arm64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x


# Memory

- memory change: 1.48x