# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_plt
- machine: darwin-arm64
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.05x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.48x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 154 ms                                                 | 182 ms: 1.18x slower                                               |
| chameleon      | 4.30 ms                                                | 4.81 ms: 1.12x slower                                              |
| docutils       | 1.43 sec                                               | 1.50 sec: 1.05x slower                                             |
| html5lib       | 33.0 ms                                                | 35.5 ms: 1.08x slower                                              |
| tornado_http   | 69.1 ms                                                | 85.4 ms: 1.24x slower                                              |
| Geometric mean | (ref)                                                  | 1.13x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none            | 282 ms                                                 | 253 ms: 1.11x faster                                               |
| async_tree_memoization_tg  | 352 ms                                                 | 324 ms: 1.09x faster                                               |
| async_tree_io_tg           | 724 ms                                                 | 676 ms: 1.07x faster                                               |
| async_tree_none_tg         | 276 ms                                                 | 261 ms: 1.06x faster                                               |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 533 ms: 1.03x faster                                               |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 523 ms: 1.01x slower                                               |
| async_tree_io              | 697 ms                                                 | 708 ms: 1.01x slower                                               |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 280 ms                                                 | 282 ms: 1.01x slower                                               |
| float          | 50.8 ms                                                | 52.6 ms: 1.04x slower                                              |
| nbody          | 61.7 ms                                                | 69.2 ms: 1.12x slower                                              |
| Geometric mean | (ref)                                                  | 1.05x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 148 ms                                                 | 152 ms: 1.03x slower                                               |
| regex_compile  | 72.8 ms                                                | 76.8 ms: 1.05x slower                                              |
| regex_effbot   | 2.43 ms                                                | 2.63 ms: 1.08x slower                                              |
| regex_v8       | 15.1 ms                                                | 17.2 ms: 1.13x slower                                              |
| Geometric mean | (ref)                                                  | 1.07x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 7.53 ms                                                | 6.51 ms: 1.16x faster                                              |
| unpickle_pure_python | 149 us                                                 | 147 us: 1.01x faster                                               |
| tomli_loads          | 1.27 sec                                               | 1.29 sec: 1.01x slower                                             |
| pickle_pure_python   | 191 us                                                 | 198 us: 1.03x slower                                               |
| pickle               | 6.98 us                                                | 7.25 us: 1.04x slower                                              |
| xml_etree_parse      | 100 ms                                                 | 107 ms: 1.06x slower                                               |
| pickle_dict          | 17.1 us                                                | 18.2 us: 1.07x slower                                              |
| xml_etree_iterparse  | 68.3 ms                                                | 74.3 ms: 1.09x slower                                              |
| unpickle             | 8.29 us                                                | 9.17 us: 1.11x slower                                              |
| pickle_list          | 2.70 us                                                | 2.99 us: 1.11x slower                                              |
| json_loads           | 15.3 us                                                | 17.1 us: 1.11x slower                                              |
| unpickle_list        | 2.69 us                                                | 3.08 us: 1.15x slower                                              |
| xml_etree_process    | 33.6 ms                                                | 39.0 ms: 1.16x slower                                              |
| xml_etree_generate   | 45.8 ms                                                | 56.2 ms: 1.23x slower                                              |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                | 17.2 ms: 1.60x slower                                              |
| python_startup_no_site | 8.57 ms                                                | 15.6 ms: 1.82x slower                                              |
| Geometric mean         | (ref)                                                  | 1.70x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 7.93 ms                                                | 6.55 ms: 1.21x faster                                              |
| genshi_text     | 14.4 ms                                                | 15.5 ms: 1.08x slower                                              |
| django_template | 20.1 ms                                                | 21.9 ms: 1.09x slower                                              |
| genshi_xml      | 28.5 ms                                                | 34.6 ms: 1.21x slower                                              |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols   | 301 us                                                 | 71.4 us: 4.21x faster                                              |
| asyncio_tcp                | 643 ms                                                 | 412 ms: 1.56x faster                                               |
| pylint                     | 253 ms                                                 | 173 ms: 1.46x faster                                               |
| mako                       | 7.93 ms                                                | 6.55 ms: 1.21x faster                                              |
| chaos                      | 47.4 ms                                                | 39.5 ms: 1.20x faster                                              |
| comprehensions             | 14.4 us                                                | 12.1 us: 1.19x faster                                              |
| json_dumps                 | 7.53 ms                                                | 6.51 ms: 1.16x faster                                              |
| async_tree_none            | 282 ms                                                 | 253 ms: 1.11x faster                                               |
| sqlglot_parse              | 890 us                                                 | 805 us: 1.11x faster                                               |
| raytrace                   | 206 ms                                                 | 187 ms: 1.10x faster                                               |
| deltablue                  | 2.75 ms                                                | 2.51 ms: 1.09x faster                                              |
| async_tree_memoization_tg  | 352 ms                                                 | 324 ms: 1.09x faster                                               |
| async_tree_io_tg           | 724 ms                                                 | 676 ms: 1.07x faster                                               |
| sympy_sum                  | 80.2 ms                                                | 75.0 ms: 1.07x faster                                              |
| generators                 | 30.3 ms                                                | 28.3 ms: 1.07x faster                                              |
| asyncio_tcp_ssl            | 1.40 sec                                               | 1.31 sec: 1.07x faster                                             |
| sqlglot_transpile          | 1.05 ms                                                | 988 us: 1.06x faster                                               |
| async_tree_none_tg         | 276 ms                                                 | 261 ms: 1.06x faster                                               |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 533 ms: 1.03x faster                                               |
| scimark_monte_carlo        | 43.5 ms                                                | 42.1 ms: 1.03x faster                                              |
| richards_super             | 37.3 ms                                                | 36.4 ms: 1.02x faster                                              |
| crypto_pyaes               | 47.5 ms                                                | 46.5 ms: 1.02x faster                                              |
| sympy_integrate            | 11.3 ms                                                | 11.1 ms: 1.02x faster                                              |
| sympy_str                  | 144 ms                                                 | 142 ms: 1.01x faster                                               |
| pprint_safe_repr           | 478 ms                                                 | 473 ms: 1.01x faster                                               |
| unpickle_pure_python       | 149 us                                                 | 147 us: 1.01x faster                                               |
| pprint_pformat             | 979 ms                                                 | 972 ms: 1.01x faster                                               |
| pidigits                   | 280 ms                                                 | 282 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 523 ms: 1.01x slower                                               |
| deepcopy_memo              | 25.7 us                                                | 26.0 us: 1.01x slower                                              |
| tomli_loads                | 1.27 sec                                               | 1.29 sec: 1.01x slower                                             |
| logging_simple             | 3.41 us                                                | 3.45 us: 1.01x slower                                              |
| create_gc_cycles           | 711 us                                                 | 719 us: 1.01x slower                                               |
| gc_traversal               | 2.38 ms                                                | 2.41 ms: 1.01x slower                                              |
| hexiom                     | 4.58 ms                                                | 4.64 ms: 1.01x slower                                              |
| go                         | 105 ms                                                 | 107 ms: 1.01x slower                                               |
| async_tree_io              | 697 ms                                                 | 708 ms: 1.01x slower                                               |
| logging_format             | 3.67 us                                                | 3.74 us: 1.02x slower                                              |
| regex_dna                  | 148 ms                                                 | 152 ms: 1.03x slower                                               |
| fannkuch                   | 240 ms                                                 | 247 ms: 1.03x slower                                               |
| pickle_pure_python         | 191 us                                                 | 198 us: 1.03x slower                                               |
| float                      | 50.8 ms                                                | 52.6 ms: 1.04x slower                                              |
| pickle                     | 6.98 us                                                | 7.25 us: 1.04x slower                                              |
| meteor_contest             | 71.1 ms                                                | 74.1 ms: 1.04x slower                                              |
| dask                       | 219 ms                                                 | 229 ms: 1.05x slower                                               |
| docutils                   | 1.43 sec                                               | 1.50 sec: 1.05x slower                                             |
| richards                   | 31.1 ms                                                | 32.6 ms: 1.05x slower                                              |
| regex_compile              | 72.8 ms                                                | 76.8 ms: 1.05x slower                                              |
| deepcopy                   | 215 us                                                 | 228 us: 1.06x slower                                               |
| gunicorn                   | 1.10 ms                                                | 1.16 ms: 1.06x slower                                              |
| xml_etree_parse            | 100 ms                                                 | 107 ms: 1.06x slower                                               |
| dulwich_log                | 28.6 ms                                                | 30.5 ms: 1.07x slower                                              |
| pickle_dict                | 17.1 us                                                | 18.2 us: 1.07x slower                                              |
| pycparser                  | 659 ms                                                 | 705 ms: 1.07x slower                                               |
| coroutines                 | 17.2 ms                                                | 18.4 ms: 1.07x slower                                              |
| sympy_expand               | 229 ms                                                 | 246 ms: 1.07x slower                                               |
| json                       | 2.75 ms                                                | 2.95 ms: 1.07x slower                                              |
| aiohttp                    | 1.02 ms                                                | 1.10 ms: 1.08x slower                                              |
| html5lib                   | 33.0 ms                                                | 35.5 ms: 1.08x slower                                              |
| scimark_sparse_mat_mult    | 2.81 ms                                                | 3.03 ms: 1.08x slower                                              |
| genshi_text                | 14.4 ms                                                | 15.5 ms: 1.08x slower                                              |
| pathlib                    | 23.2 ms                                                | 25.0 ms: 1.08x slower                                              |
| mdp                        | 1.48 sec                                               | 1.60 sec: 1.08x slower                                             |
| coverage                   | 43.9 ms                                                | 47.5 ms: 1.08x slower                                              |
| regex_effbot               | 2.43 ms                                                | 2.63 ms: 1.08x slower                                              |
| logging_silent             | 66.5 ns                                                | 72.1 ns: 1.08x slower                                              |
| django_template            | 20.1 ms                                                | 21.9 ms: 1.09x slower                                              |
| xml_etree_iterparse        | 68.3 ms                                                | 74.3 ms: 1.09x slower                                              |
| bench_thread_pool          | 465 us                                                 | 508 us: 1.09x slower                                               |
| spectral_norm              | 65.7 ms                                                | 72.2 ms: 1.10x slower                                              |
| deepcopy_reduce            | 1.79 us                                                | 1.97 us: 1.10x slower                                              |
| unpickle                   | 8.29 us                                                | 9.17 us: 1.11x slower                                              |
| pickle_list                | 2.70 us                                                | 2.99 us: 1.11x slower                                              |
| json_loads                 | 15.3 us                                                | 17.1 us: 1.11x slower                                              |
| sqlglot_normalize          | 162 ms                                                 | 181 ms: 1.12x slower                                               |
| chameleon                  | 4.30 ms                                                | 4.81 ms: 1.12x slower                                              |
| nbody                      | 61.7 ms                                                | 69.2 ms: 1.12x slower                                              |
| pyflate                    | 284 ms                                                 | 318 ms: 1.12x slower                                               |
| nqueens                    | 55.9 ms                                                | 63.1 ms: 1.13x slower                                              |
| scimark_fft                | 173 ms                                                 | 195 ms: 1.13x slower                                               |
| thrift                     | 410 us                                                 | 464 us: 1.13x slower                                               |
| regex_v8                   | 15.1 ms                                                | 17.2 ms: 1.13x slower                                              |
| unpickle_list              | 2.69 us                                                | 3.08 us: 1.15x slower                                              |
| xml_etree_process          | 33.6 ms                                                | 39.0 ms: 1.16x slower                                              |
| sqlglot_optimize           | 29.6 ms                                                | 34.5 ms: 1.16x slower                                              |
| 2to3                       | 154 ms                                                 | 182 ms: 1.18x slower                                               |
| genshi_xml                 | 28.5 ms                                                | 34.6 ms: 1.21x slower                                              |
| xml_etree_generate         | 45.8 ms                                                | 56.2 ms: 1.23x slower                                              |
| tornado_http               | 69.1 ms                                                | 85.4 ms: 1.24x slower                                              |
| scimark_lu                 | 67.7 ms                                                | 83.9 ms: 1.24x slower                                              |
| bench_mp_pool              | 41.0 ms                                                | 51.3 ms: 1.25x slower                                              |
| sqlite_synth               | 1.26 us                                                | 1.59 us: 1.26x slower                                              |
| scimark_sor                | 79.2 ms                                                | 110 ms: 1.39x slower                                               |
| telco                      | 3.17 ms                                                | 4.44 ms: 1.40x slower                                              |
| python_startup             | 10.8 ms                                                | 17.2 ms: 1.60x slower                                              |
| async_generators           | 192 ms                                                 | 311 ms: 1.62x slower                                               |
| mypy2                      | 372 ms                                                 | 608 ms: 1.63x slower                                               |
| python_startup_no_site     | 8.57 ms                                                | 15.6 ms: 1.82x slower                                              |
| unpack_sequence            | 33.6 ns                                                | 72.7 ns: 2.16x slower                                              |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                       |

Benchmark hidden because not significant (2): async_tree_memoization, asyncio_websockets
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (8) of results/bm-20240315-3.13.0a5+-9242976-JIT/bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg


# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x


# Memory

- memory change: 1.48x