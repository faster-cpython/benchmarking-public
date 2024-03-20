# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: darwin-arm64
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 154 ms                                                 | 188 ms: 1.22x slower                                                         |
| chameleon      | 4.30 ms                                                | 4.82 ms: 1.12x slower                                                        |
| docutils       | 1.43 sec                                               | 1.54 sec: 1.08x slower                                                       |
| html5lib       | 33.0 ms                                                | 35.8 ms: 1.09x slower                                                        |
| tornado_http   | 69.1 ms                                                | 84.9 ms: 1.23x slower                                                        |
| Geometric mean | (ref)                                                  | 1.15x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 282 ms                                                 | 254 ms: 1.11x faster                                                         |
| async_tree_memoization_tg  | 352 ms                                                 | 324 ms: 1.09x faster                                                         |
| async_tree_io_tg           | 724 ms                                                 | 676 ms: 1.07x faster                                                         |
| async_tree_none_tg         | 276 ms                                                 | 260 ms: 1.06x faster                                                         |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 532 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 523 ms: 1.01x slower                                                         |
| async_tree_io              | 697 ms                                                 | 706 ms: 1.01x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 280 ms                                                 | 282 ms: 1.01x slower                                                         |
| float          | 50.8 ms                                                | 53.1 ms: 1.04x slower                                                        |
| nbody          | 61.7 ms                                                | 70.8 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 148 ms                                                 | 152 ms: 1.03x slower                                                         |
| regex_effbot   | 2.43 ms                                                | 2.63 ms: 1.08x slower                                                        |
| regex_v8       | 15.1 ms                                                | 17.2 ms: 1.14x slower                                                        |
| regex_compile  | 72.8 ms                                                | 85.4 ms: 1.17x slower                                                        |
| Geometric mean | (ref)                                                  | 1.10x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 7.53 ms                                                | 6.53 ms: 1.15x faster                                                        |
| unpickle_pure_python | 149 us                                                 | 151 us: 1.02x slower                                                         |
| pickle_pure_python   | 191 us                                                 | 196 us: 1.02x slower                                                         |
| pickle               | 6.98 us                                                | 7.29 us: 1.04x slower                                                        |
| xml_etree_parse      | 100 ms                                                 | 106 ms: 1.06x slower                                                         |
| pickle_dict          | 17.1 us                                                | 18.2 us: 1.06x slower                                                        |
| tomli_loads          | 1.27 sec                                               | 1.36 sec: 1.07x slower                                                       |
| xml_etree_iterparse  | 68.3 ms                                                | 74.7 ms: 1.09x slower                                                        |
| unpickle             | 8.29 us                                                | 9.15 us: 1.10x slower                                                        |
| pickle_list          | 2.70 us                                                | 2.98 us: 1.10x slower                                                        |
| json_loads           | 15.3 us                                                | 17.1 us: 1.11x slower                                                        |
| unpickle_list        | 2.69 us                                                | 3.06 us: 1.14x slower                                                        |
| xml_etree_process    | 33.6 ms                                                | 39.0 ms: 1.16x slower                                                        |
| xml_etree_generate   | 45.8 ms                                                | 56.8 ms: 1.24x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                | 20.6 ms: 1.92x slower                                                        |
| python_startup_no_site | 8.57 ms                                                | 18.9 ms: 2.21x slower                                                        |
| Geometric mean         | (ref)                                                  | 2.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 7.93 ms                                                | 6.73 ms: 1.18x faster                                                        |
| genshi_text     | 14.4 ms                                                | 15.8 ms: 1.09x slower                                                        |
| django_template | 20.1 ms                                                | 22.1 ms: 1.10x slower                                                        |
| genshi_xml      | 28.5 ms                                                | 37.7 ms: 1.32x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.08x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols   | 301 us                                                 | 71.7 us: 4.20x faster                                                        |
| pylint                     | 253 ms                                                 | 176 ms: 1.43x faster                                                         |
| asyncio_tcp                | 643 ms                                                 | 461 ms: 1.39x faster                                                         |
| chaos                      | 47.4 ms                                                | 40.1 ms: 1.18x faster                                                        |
| mako                       | 7.93 ms                                                | 6.73 ms: 1.18x faster                                                        |
| json_dumps                 | 7.53 ms                                                | 6.53 ms: 1.15x faster                                                        |
| comprehensions             | 14.4 us                                                | 12.7 us: 1.14x faster                                                        |
| async_tree_none            | 282 ms                                                 | 254 ms: 1.11x faster                                                         |
| async_tree_memoization_tg  | 352 ms                                                 | 324 ms: 1.09x faster                                                         |
| deltablue                  | 2.75 ms                                                | 2.54 ms: 1.08x faster                                                        |
| async_tree_io_tg           | 724 ms                                                 | 676 ms: 1.07x faster                                                         |
| raytrace                   | 206 ms                                                 | 192 ms: 1.07x faster                                                         |
| asyncio_tcp_ssl            | 1.40 sec                                               | 1.31 sec: 1.07x faster                                                       |
| generators                 | 30.3 ms                                                | 28.4 ms: 1.07x faster                                                        |
| async_tree_none_tg         | 276 ms                                                 | 260 ms: 1.06x faster                                                         |
| sqlglot_parse              | 890 us                                                 | 840 us: 1.06x faster                                                         |
| sympy_sum                  | 80.2 ms                                                | 77.4 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 532 ms: 1.03x faster                                                         |
| sqlglot_transpile          | 1.05 ms                                                | 1.03 ms: 1.03x faster                                                        |
| create_gc_cycles           | 711 us                                                 | 713 us: 1.00x slower                                                         |
| sympy_str                  | 144 ms                                                 | 145 ms: 1.01x slower                                                         |
| pidigits                   | 280 ms                                                 | 282 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 523 ms: 1.01x slower                                                         |
| crypto_pyaes               | 47.5 ms                                                | 47.9 ms: 1.01x slower                                                        |
| gc_traversal               | 2.38 ms                                                | 2.41 ms: 1.01x slower                                                        |
| async_tree_io              | 697 ms                                                 | 706 ms: 1.01x slower                                                         |
| deepcopy_memo              | 25.7 us                                                | 26.2 us: 1.02x slower                                                        |
| unpickle_pure_python       | 149 us                                                 | 151 us: 1.02x slower                                                         |
| sympy_integrate            | 11.3 ms                                                | 11.5 ms: 1.02x slower                                                        |
| logging_simple             | 3.41 us                                                | 3.49 us: 1.02x slower                                                        |
| scimark_monte_carlo        | 43.5 ms                                                | 44.5 ms: 1.02x slower                                                        |
| pickle_pure_python         | 191 us                                                 | 196 us: 1.02x slower                                                         |
| logging_format             | 3.67 us                                                | 3.76 us: 1.02x slower                                                        |
| regex_dna                  | 148 ms                                                 | 152 ms: 1.03x slower                                                         |
| dask                       | 219 ms                                                 | 228 ms: 1.04x slower                                                         |
| float                      | 50.8 ms                                                | 53.1 ms: 1.04x slower                                                        |
| pickle                     | 6.98 us                                                | 7.29 us: 1.04x slower                                                        |
| meteor_contest             | 71.1 ms                                                | 75.3 ms: 1.06x slower                                                        |
| xml_etree_parse            | 100 ms                                                 | 106 ms: 1.06x slower                                                         |
| pickle_dict                | 17.1 us                                                | 18.2 us: 1.06x slower                                                        |
| deepcopy                   | 215 us                                                 | 229 us: 1.06x slower                                                         |
| tomli_loads                | 1.27 sec                                               | 1.36 sec: 1.07x slower                                                       |
| dulwich_log                | 28.6 ms                                                | 30.7 ms: 1.07x slower                                                        |
| json                       | 2.75 ms                                                | 2.96 ms: 1.07x slower                                                        |
| coroutines                 | 17.2 ms                                                | 18.4 ms: 1.07x slower                                                        |
| docutils                   | 1.43 sec                                               | 1.54 sec: 1.08x slower                                                       |
| pprint_safe_repr           | 478 ms                                                 | 515 ms: 1.08x slower                                                         |
| aiohttp                    | 1.02 ms                                                | 1.10 ms: 1.08x slower                                                        |
| gunicorn                   | 1.10 ms                                                | 1.18 ms: 1.08x slower                                                        |
| pprint_pformat             | 979 ms                                                 | 1.06 sec: 1.08x slower                                                       |
| sympy_expand               | 229 ms                                                 | 247 ms: 1.08x slower                                                         |
| regex_effbot               | 2.43 ms                                                | 2.63 ms: 1.08x slower                                                        |
| coverage                   | 43.9 ms                                                | 47.6 ms: 1.08x slower                                                        |
| html5lib                   | 33.0 ms                                                | 35.8 ms: 1.09x slower                                                        |
| pathlib                    | 23.2 ms                                                | 25.2 ms: 1.09x slower                                                        |
| logging_silent             | 66.5 ns                                                | 72.3 ns: 1.09x slower                                                        |
| go                         | 105 ms                                                 | 115 ms: 1.09x slower                                                         |
| genshi_text                | 14.4 ms                                                | 15.8 ms: 1.09x slower                                                        |
| xml_etree_iterparse        | 68.3 ms                                                | 74.7 ms: 1.09x slower                                                        |
| django_template            | 20.1 ms                                                | 22.1 ms: 1.10x slower                                                        |
| bench_thread_pool          | 465 us                                                 | 512 us: 1.10x slower                                                         |
| deepcopy_reduce            | 1.79 us                                                | 1.98 us: 1.10x slower                                                        |
| pycparser                  | 659 ms                                                 | 727 ms: 1.10x slower                                                         |
| mdp                        | 1.48 sec                                               | 1.64 sec: 1.10x slower                                                       |
| unpickle                   | 8.29 us                                                | 9.15 us: 1.10x slower                                                        |
| pickle_list                | 2.70 us                                                | 2.98 us: 1.10x slower                                                        |
| json_loads                 | 15.3 us                                                | 17.1 us: 1.11x slower                                                        |
| hexiom                     | 4.58 ms                                                | 5.12 ms: 1.12x slower                                                        |
| scimark_sparse_mat_mult    | 2.81 ms                                                | 3.15 ms: 1.12x slower                                                        |
| chameleon                  | 4.30 ms                                                | 4.82 ms: 1.12x slower                                                        |
| thrift                     | 410 us                                                 | 460 us: 1.12x slower                                                         |
| richards_super             | 37.3 ms                                                | 42.1 ms: 1.13x slower                                                        |
| sqlglot_normalize          | 162 ms                                                 | 183 ms: 1.13x slower                                                         |
| regex_v8                   | 15.1 ms                                                | 17.2 ms: 1.14x slower                                                        |
| nqueens                    | 55.9 ms                                                | 63.7 ms: 1.14x slower                                                        |
| unpickle_list              | 2.69 us                                                | 3.06 us: 1.14x slower                                                        |
| nbody                      | 61.7 ms                                                | 70.8 ms: 1.15x slower                                                        |
| scimark_fft                | 173 ms                                                 | 199 ms: 1.16x slower                                                         |
| spectral_norm              | 65.7 ms                                                | 76.0 ms: 1.16x slower                                                        |
| xml_etree_process          | 33.6 ms                                                | 39.0 ms: 1.16x slower                                                        |
| regex_compile              | 72.8 ms                                                | 85.4 ms: 1.17x slower                                                        |
| sqlglot_optimize           | 29.6 ms                                                | 35.5 ms: 1.20x slower                                                        |
| richards                   | 31.1 ms                                                | 37.7 ms: 1.21x slower                                                        |
| 2to3                       | 154 ms                                                 | 188 ms: 1.22x slower                                                         |
| pyflate                    | 284 ms                                                 | 348 ms: 1.23x slower                                                         |
| tornado_http               | 69.1 ms                                                | 84.9 ms: 1.23x slower                                                        |
| xml_etree_generate         | 45.8 ms                                                | 56.8 ms: 1.24x slower                                                        |
| scimark_lu                 | 67.7 ms                                                | 85.6 ms: 1.26x slower                                                        |
| sqlite_synth               | 1.26 us                                                | 1.59 us: 1.27x slower                                                        |
| fannkuch                   | 240 ms                                                 | 314 ms: 1.31x slower                                                         |
| genshi_xml                 | 28.5 ms                                                | 37.7 ms: 1.32x slower                                                        |
| bench_mp_pool              | 41.0 ms                                                | 56.1 ms: 1.37x slower                                                        |
| scimark_sor                | 79.2 ms                                                | 113 ms: 1.42x slower                                                         |
| telco                      | 3.17 ms                                                | 4.58 ms: 1.44x slower                                                        |
| async_generators           | 192 ms                                                 | 314 ms: 1.63x slower                                                         |
| mypy2                      | 372 ms                                                 | 617 ms: 1.66x slower                                                         |
| python_startup             | 10.8 ms                                                | 20.6 ms: 1.92x slower                                                        |
| python_startup_no_site     | 8.57 ms                                                | 18.9 ms: 2.21x slower                                                        |
| unpack_sequence            | 33.6 ns                                                | 113 ns: 3.35x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.08x slower                                                                 |

Benchmark hidden because not significant (2): async_tree_memoization, asyncio_websockets
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (8) of results/bm-20240318-3.13.0a5+-c8d6017-JIT/bm-20240318-darwin-arm64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.03x


# Memory

- memory change: 1.90x