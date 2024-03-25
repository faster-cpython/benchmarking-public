# Results vs. 3.11.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: darwin-arm64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.02x faster
- HPT reliability: 79.53%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 154 ms                                                 | 164 ms: 1.07x slower                                                   |
| chameleon      | 4.30 ms                                                | 4.46 ms: 1.04x slower                                                  |
| docutils       | 1.43 sec                                               | 1.48 sec: 1.04x slower                                                 |
| html5lib       | 33.0 ms                                                | 34.0 ms: 1.03x slower                                                  |
| tornado_http   | 69.1 ms                                                | 81.6 ms: 1.18x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 352 ms                                                 | 241 ms: 1.46x faster                                                   |
| async_tree_memoization     | 336 ms                                                 | 251 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 276 ms                                                 | 208 ms: 1.33x faster                                                   |
| async_tree_none            | 282 ms                                                 | 220 ms: 1.28x faster                                                   |
| async_tree_io_tg           | 724 ms                                                 | 575 ms: 1.26x faster                                                   |
| async_tree_io              | 697 ms                                                 | 561 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 451 ms: 1.22x faster                                                   |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 455 ms: 1.14x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 50.8 ms                                                | 51.2 ms: 1.01x slower                                                  |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| nbody          | 61.7 ms                                                | 71.0 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 72.8 ms                                                | 70.0 ms: 1.04x faster                                                  |
| regex_dna      | 148 ms                                                 | 152 ms: 1.02x slower                                                   |
| regex_effbot   | 2.43 ms                                                | 2.54 ms: 1.05x slower                                                  |
| regex_v8       | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.53 ms                                                | 6.36 ms: 1.18x faster                                                  |
| pickle_pure_python   | 191 us                                                 | 185 us: 1.04x faster                                                   |
| xml_etree_parse      | 100 ms                                                 | 99.4 ms: 1.01x faster                                                  |
| unpickle_pure_python | 149 us                                                 | 148 us: 1.01x faster                                                   |
| xml_etree_iterparse  | 68.3 ms                                                | 69.6 ms: 1.02x slower                                                  |
| pickle               | 6.98 us                                                | 7.25 us: 1.04x slower                                                  |
| pickle_dict          | 17.1 us                                                | 18.1 us: 1.06x slower                                                  |
| pickle_list          | 2.70 us                                                | 2.95 us: 1.10x slower                                                  |
| unpickle             | 8.29 us                                                | 9.17 us: 1.11x slower                                                  |
| json_loads           | 15.3 us                                                | 17.0 us: 1.11x slower                                                  |
| xml_etree_process    | 33.6 ms                                                | 37.5 ms: 1.12x slower                                                  |
| unpickle_list        | 2.69 us                                                | 3.05 us: 1.13x slower                                                  |
| xml_etree_generate   | 45.8 ms                                                | 54.6 ms: 1.19x slower                                                  |
| tomli_loads          | 1.27 sec                                               | 1.52 sec: 1.19x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                | 14.9 ms: 1.39x slower                                                  |
| python_startup_no_site | 8.57 ms                                                | 13.0 ms: 1.52x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.45x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.93 ms                                                | 7.06 ms: 1.12x faster                                                  |
| genshi_text     | 14.4 ms                                                | 14.4 ms: 1.00x faster                                                  |
| django_template | 20.1 ms                                                | 20.3 ms: 1.01x slower                                                  |
| genshi_xml      | 28.5 ms                                                | 31.2 ms: 1.09x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 301 us                                                 | 69.7 us: 4.32x faster                                                  |
| asyncio_tcp                | 643 ms                                                 | 399 ms: 1.61x faster                                                   |
| pylint                     | 253 ms                                                 | 168 ms: 1.51x faster                                                   |
| async_tree_memoization_tg  | 352 ms                                                 | 241 ms: 1.46x faster                                                   |
| async_tree_memoization     | 336 ms                                                 | 251 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 276 ms                                                 | 208 ms: 1.33x faster                                                   |
| raytrace                   | 206 ms                                                 | 156 ms: 1.32x faster                                                   |
| comprehensions             | 14.4 us                                                | 11.2 us: 1.29x faster                                                  |
| chaos                      | 47.4 ms                                                | 36.9 ms: 1.28x faster                                                  |
| async_tree_none            | 282 ms                                                 | 220 ms: 1.28x faster                                                   |
| unpack_sequence            | 33.6 ns                                                | 26.5 ns: 1.27x faster                                                  |
| async_tree_io_tg           | 724 ms                                                 | 575 ms: 1.26x faster                                                   |
| async_tree_io              | 697 ms                                                 | 561 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 451 ms: 1.22x faster                                                   |
| deltablue                  | 2.75 ms                                                | 2.27 ms: 1.21x faster                                                  |
| sqlglot_parse              | 890 us                                                 | 748 us: 1.19x faster                                                   |
| json_dumps                 | 7.53 ms                                                | 6.36 ms: 1.18x faster                                                  |
| sqlglot_transpile          | 1.05 ms                                                | 909 us: 1.16x faster                                                   |
| sympy_sum                  | 80.2 ms                                                | 70.0 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 455 ms: 1.14x faster                                                   |
| mako                       | 7.93 ms                                                | 7.06 ms: 1.12x faster                                                  |
| generators                 | 30.3 ms                                                | 27.1 ms: 1.12x faster                                                  |
| sympy_integrate            | 11.3 ms                                                | 10.3 ms: 1.09x faster                                                  |
| deepcopy_memo              | 25.7 us                                                | 23.6 us: 1.09x faster                                                  |
| hexiom                     | 4.58 ms                                                | 4.20 ms: 1.09x faster                                                  |
| sympy_str                  | 144 ms                                                 | 132 ms: 1.09x faster                                                   |
| asyncio_tcp_ssl            | 1.40 sec                                               | 1.31 sec: 1.07x faster                                                 |
| go                         | 105 ms                                                 | 101 ms: 1.05x faster                                                   |
| richards_super             | 37.3 ms                                                | 35.7 ms: 1.04x faster                                                  |
| regex_compile              | 72.8 ms                                                | 70.0 ms: 1.04x faster                                                  |
| logging_simple             | 3.41 us                                                | 3.29 us: 1.04x faster                                                  |
| pickle_pure_python         | 191 us                                                 | 185 us: 1.04x faster                                                   |
| logging_format             | 3.67 us                                                | 3.55 us: 1.03x faster                                                  |
| logging_silent             | 66.5 ns                                                | 65.1 ns: 1.02x faster                                                  |
| deepcopy                   | 215 us                                                 | 213 us: 1.01x faster                                                   |
| xml_etree_parse            | 100 ms                                                 | 99.4 ms: 1.01x faster                                                  |
| crypto_pyaes               | 47.5 ms                                                | 47.1 ms: 1.01x faster                                                  |
| pprint_pformat             | 979 ms                                                 | 972 ms: 1.01x faster                                                   |
| unpickle_pure_python       | 149 us                                                 | 148 us: 1.01x faster                                                   |
| genshi_text                | 14.4 ms                                                | 14.4 ms: 1.00x faster                                                  |
| sympy_expand               | 229 ms                                                 | 228 ms: 1.00x faster                                                   |
| meteor_contest             | 71.1 ms                                                | 71.2 ms: 1.00x slower                                                  |
| gc_traversal               | 2.38 ms                                                | 2.39 ms: 1.00x slower                                                  |
| django_template            | 20.1 ms                                                | 20.3 ms: 1.01x slower                                                  |
| float                      | 50.8 ms                                                | 51.2 ms: 1.01x slower                                                  |
| coroutines                 | 17.2 ms                                                | 17.3 ms: 1.01x slower                                                  |
| pidigits                   | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| scimark_lu                 | 67.7 ms                                                | 68.5 ms: 1.01x slower                                                  |
| xml_etree_iterparse        | 68.3 ms                                                | 69.6 ms: 1.02x slower                                                  |
| regex_dna                  | 148 ms                                                 | 152 ms: 1.02x slower                                                   |
| bench_thread_pool          | 465 us                                                 | 477 us: 1.02x slower                                                   |
| scimark_monte_carlo        | 43.5 ms                                                | 44.6 ms: 1.02x slower                                                  |
| mdp                        | 1.48 sec                                               | 1.52 sec: 1.03x slower                                                 |
| html5lib                   | 33.0 ms                                                | 34.0 ms: 1.03x slower                                                  |
| deepcopy_reduce            | 1.79 us                                                | 1.86 us: 1.03x slower                                                  |
| docutils                   | 1.43 sec                                               | 1.48 sec: 1.04x slower                                                 |
| chameleon                  | 4.30 ms                                                | 4.46 ms: 1.04x slower                                                  |
| pickle                     | 6.98 us                                                | 7.25 us: 1.04x slower                                                  |
| aiohttp                    | 1.02 ms                                                | 1.07 ms: 1.04x slower                                                  |
| richards                   | 31.1 ms                                                | 32.3 ms: 1.04x slower                                                  |
| regex_effbot               | 2.43 ms                                                | 2.54 ms: 1.05x slower                                                  |
| sqlglot_normalize          | 162 ms                                                 | 171 ms: 1.06x slower                                                   |
| pickle_dict                | 17.1 us                                                | 18.1 us: 1.06x slower                                                  |
| pathlib                    | 23.2 ms                                                | 24.7 ms: 1.07x slower                                                  |
| json                       | 2.75 ms                                                | 2.93 ms: 1.07x slower                                                  |
| 2to3                       | 154 ms                                                 | 164 ms: 1.07x slower                                                   |
| scimark_sparse_mat_mult    | 2.81 ms                                                | 3.02 ms: 1.07x slower                                                  |
| sqlglot_optimize           | 29.6 ms                                                | 31.9 ms: 1.08x slower                                                  |
| coverage                   | 43.9 ms                                                | 47.2 ms: 1.08x slower                                                  |
| thrift                     | 410 us                                                 | 442 us: 1.08x slower                                                   |
| spectral_norm              | 65.7 ms                                                | 71.3 ms: 1.08x slower                                                  |
| genshi_xml                 | 28.5 ms                                                | 31.2 ms: 1.09x slower                                                  |
| pickle_list                | 2.70 us                                                | 2.95 us: 1.10x slower                                                  |
| bench_mp_pool              | 41.0 ms                                                | 45.1 ms: 1.10x slower                                                  |
| unpickle                   | 8.29 us                                                | 9.17 us: 1.11x slower                                                  |
| json_loads                 | 15.3 us                                                | 17.0 us: 1.11x slower                                                  |
| fannkuch                   | 240 ms                                                 | 266 ms: 1.11x slower                                                   |
| xml_etree_process          | 33.6 ms                                                | 37.5 ms: 1.12x slower                                                  |
| regex_v8                   | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                  |
| unpickle_list              | 2.69 us                                                | 3.05 us: 1.13x slower                                                  |
| scimark_fft                | 173 ms                                                 | 197 ms: 1.14x slower                                                   |
| nbody                      | 61.7 ms                                                | 71.0 ms: 1.15x slower                                                  |
| pyflate                    | 284 ms                                                 | 329 ms: 1.16x slower                                                   |
| tornado_http               | 69.1 ms                                                | 81.6 ms: 1.18x slower                                                  |
| xml_etree_generate         | 45.8 ms                                                | 54.6 ms: 1.19x slower                                                  |
| tomli_loads                | 1.27 sec                                               | 1.52 sec: 1.19x slower                                                 |
| sqlite_synth               | 1.26 us                                                | 1.56 us: 1.24x slower                                                  |
| mypy2                      | 372 ms                                                 | 466 ms: 1.25x slower                                                   |
| scimark_sor                | 79.2 ms                                                | 100 ms: 1.27x slower                                                   |
| python_startup             | 10.8 ms                                                | 14.9 ms: 1.39x slower                                                  |
| telco                      | 3.17 ms                                                | 4.53 ms: 1.43x slower                                                  |
| async_generators           | 192 ms                                                 | 286 ms: 1.49x slower                                                   |
| python_startup_no_site     | 8.57 ms                                                | 13.0 ms: 1.52x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (8): gunicorn, dulwich_log, asyncio_websockets, nqueens, pprint_safe_repr, pycparser, create_gc_cycles, dask
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (8) of results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg


# HPT report

- Reliability score: 79.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.07x