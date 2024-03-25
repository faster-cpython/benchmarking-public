# Results vs. 3.11.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: darwin-arm64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.02x slower
- HPT reliability: 96.41%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 154 ms                                                 | 176 ms: 1.14x slower                                                   |
| chameleon      | 4.30 ms                                                | 4.41 ms: 1.03x slower                                                  |
| docutils       | 1.43 sec                                               | 1.54 sec: 1.07x slower                                                 |
| html5lib       | 33.0 ms                                                | 32.0 ms: 1.03x faster                                                  |
| tornado_http   | 69.1 ms                                                | 79.5 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 352 ms                                                 | 242 ms: 1.46x faster                                                   |
| async_tree_none_tg         | 276 ms                                                 | 207 ms: 1.33x faster                                                   |
| async_tree_memoization     | 336 ms                                                 | 254 ms: 1.32x faster                                                   |
| async_tree_none            | 282 ms                                                 | 221 ms: 1.27x faster                                                   |
| async_tree_io_tg           | 724 ms                                                 | 574 ms: 1.26x faster                                                   |
| async_tree_io              | 697 ms                                                 | 567 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 449 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 455 ms: 1.14x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 50.8 ms                                                | 49.2 ms: 1.03x faster                                                  |
| pidigits       | 280 ms                                                 | 282 ms: 1.01x slower                                                   |
| nbody          | 61.7 ms                                                | 70.2 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 148 ms                                                 | 145 ms: 1.02x faster                                                   |
| regex_effbot   | 2.43 ms                                                | 2.55 ms: 1.05x slower                                                  |
| regex_v8       | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                  |
| regex_compile  | 72.8 ms                                                | 83.5 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.53 ms                                                | 6.35 ms: 1.19x faster                                                  |
| unpickle_pure_python | 149 us                                                 | 142 us: 1.05x faster                                                   |
| pickle_pure_python   | 191 us                                                 | 183 us: 1.04x faster                                                   |
| xml_etree_parse      | 100 ms                                                 | 98.8 ms: 1.02x faster                                                  |
| tomli_loads          | 1.27 sec                                               | 1.28 sec: 1.01x slower                                                 |
| xml_etree_iterparse  | 68.3 ms                                                | 70.0 ms: 1.03x slower                                                  |
| pickle               | 6.98 us                                                | 7.20 us: 1.03x slower                                                  |
| pickle_dict          | 17.1 us                                                | 18.1 us: 1.06x slower                                                  |
| xml_etree_process    | 33.6 ms                                                | 36.7 ms: 1.09x slower                                                  |
| pickle_list          | 2.70 us                                                | 2.96 us: 1.10x slower                                                  |
| json_loads           | 15.3 us                                                | 17.0 us: 1.11x slower                                                  |
| unpickle             | 8.29 us                                                | 9.25 us: 1.12x slower                                                  |
| unpickle_list        | 2.69 us                                                | 3.03 us: 1.13x slower                                                  |
| xml_etree_generate   | 45.8 ms                                                | 54.0 ms: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                | 18.9 ms: 1.75x slower                                                  |
| python_startup_no_site | 8.57 ms                                                | 17.1 ms: 1.99x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.87x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.93 ms                                                | 6.89 ms: 1.15x faster                                                  |
| genshi_text     | 14.4 ms                                                | 14.6 ms: 1.01x slower                                                  |
| django_template | 20.1 ms                                                | 20.8 ms: 1.03x slower                                                  |
| genshi_xml      | 28.5 ms                                                | 32.9 ms: 1.15x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 301 us                                                 | 69.8 us: 4.31x faster                                                  |
| asyncio_tcp                | 643 ms                                                 | 410 ms: 1.57x faster                                                   |
| async_tree_memoization_tg  | 352 ms                                                 | 242 ms: 1.46x faster                                                   |
| pylint                     | 253 ms                                                 | 178 ms: 1.42x faster                                                   |
| async_tree_none_tg         | 276 ms                                                 | 207 ms: 1.33x faster                                                   |
| async_tree_memoization     | 336 ms                                                 | 254 ms: 1.32x faster                                                   |
| async_tree_none            | 282 ms                                                 | 221 ms: 1.27x faster                                                   |
| async_tree_io_tg           | 724 ms                                                 | 574 ms: 1.26x faster                                                   |
| chaos                      | 47.4 ms                                                | 38.1 ms: 1.24x faster                                                  |
| async_tree_io              | 697 ms                                                 | 567 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 449 ms: 1.23x faster                                                   |
| comprehensions             | 14.4 us                                                | 12.0 us: 1.21x faster                                                  |
| json_dumps                 | 7.53 ms                                                | 6.35 ms: 1.19x faster                                                  |
| deltablue                  | 2.75 ms                                                | 2.36 ms: 1.16x faster                                                  |
| sqlglot_parse              | 890 us                                                 | 768 us: 1.16x faster                                                   |
| raytrace                   | 206 ms                                                 | 178 ms: 1.15x faster                                                   |
| mako                       | 7.93 ms                                                | 6.89 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 455 ms: 1.14x faster                                                   |
| sqlglot_transpile          | 1.05 ms                                                | 938 us: 1.12x faster                                                   |
| generators                 | 30.3 ms                                                | 27.1 ms: 1.12x faster                                                  |
| asyncio_tcp_ssl            | 1.40 sec                                               | 1.31 sec: 1.07x faster                                                 |
| richards_super             | 37.3 ms                                                | 35.0 ms: 1.06x faster                                                  |
| deepcopy_memo              | 25.7 us                                                | 24.2 us: 1.06x faster                                                  |
| sympy_sum                  | 80.2 ms                                                | 76.0 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 149 us                                                 | 142 us: 1.05x faster                                                   |
| logging_simple             | 3.41 us                                                | 3.26 us: 1.05x faster                                                  |
| pickle_pure_python         | 191 us                                                 | 183 us: 1.04x faster                                                   |
| logging_format             | 3.67 us                                                | 3.54 us: 1.04x faster                                                  |
| float                      | 50.8 ms                                                | 49.2 ms: 1.03x faster                                                  |
| html5lib                   | 33.0 ms                                                | 32.0 ms: 1.03x faster                                                  |
| sympy_str                  | 144 ms                                                 | 140 ms: 1.03x faster                                                   |
| regex_dna                  | 148 ms                                                 | 145 ms: 1.02x faster                                                   |
| xml_etree_parse            | 100 ms                                                 | 98.8 ms: 1.02x faster                                                  |
| logging_silent             | 66.5 ns                                                | 65.6 ns: 1.01x faster                                                  |
| crypto_pyaes               | 47.5 ms                                                | 46.9 ms: 1.01x faster                                                  |
| go                         | 105 ms                                                 | 105 ms: 1.00x faster                                                   |
| sympy_integrate            | 11.3 ms                                                | 11.2 ms: 1.00x faster                                                  |
| coroutines                 | 17.2 ms                                                | 17.2 ms: 1.00x slower                                                  |
| pidigits                   | 280 ms                                                 | 282 ms: 1.01x slower                                                   |
| gc_traversal               | 2.38 ms                                                | 2.40 ms: 1.01x slower                                                  |
| tomli_loads                | 1.27 sec                                               | 1.28 sec: 1.01x slower                                                 |
| richards                   | 31.1 ms                                                | 31.4 ms: 1.01x slower                                                  |
| genshi_text                | 14.4 ms                                                | 14.6 ms: 1.01x slower                                                  |
| create_gc_cycles           | 711 us                                                 | 719 us: 1.01x slower                                                   |
| pycparser                  | 659 ms                                                 | 670 ms: 1.02x slower                                                   |
| scimark_monte_carlo        | 43.5 ms                                                | 44.5 ms: 1.02x slower                                                  |
| dask                       | 219 ms                                                 | 225 ms: 1.02x slower                                                   |
| xml_etree_iterparse        | 68.3 ms                                                | 70.0 ms: 1.03x slower                                                  |
| chameleon                  | 4.30 ms                                                | 4.41 ms: 1.03x slower                                                  |
| sympy_expand               | 229 ms                                                 | 236 ms: 1.03x slower                                                   |
| django_template            | 20.1 ms                                                | 20.8 ms: 1.03x slower                                                  |
| meteor_contest             | 71.1 ms                                                | 73.3 ms: 1.03x slower                                                  |
| pickle                     | 6.98 us                                                | 7.20 us: 1.03x slower                                                  |
| deepcopy_reduce            | 1.79 us                                                | 1.86 us: 1.03x slower                                                  |
| dulwich_log                | 28.6 ms                                                | 29.6 ms: 1.04x slower                                                  |
| pprint_safe_repr           | 478 ms                                                 | 497 ms: 1.04x slower                                                   |
| pprint_pformat             | 979 ms                                                 | 1.02 sec: 1.04x slower                                                 |
| regex_effbot               | 2.43 ms                                                | 2.55 ms: 1.05x slower                                                  |
| bench_thread_pool          | 465 us                                                 | 491 us: 1.06x slower                                                   |
| mdp                        | 1.48 sec                                               | 1.57 sec: 1.06x slower                                                 |
| gunicorn                   | 1.10 ms                                                | 1.16 ms: 1.06x slower                                                  |
| coverage                   | 43.9 ms                                                | 46.5 ms: 1.06x slower                                                  |
| pickle_dict                | 17.1 us                                                | 18.1 us: 1.06x slower                                                  |
| hexiom                     | 4.58 ms                                                | 4.86 ms: 1.06x slower                                                  |
| pathlib                    | 23.2 ms                                                | 24.6 ms: 1.06x slower                                                  |
| thrift                     | 410 us                                                 | 436 us: 1.06x slower                                                   |
| docutils                   | 1.43 sec                                               | 1.54 sec: 1.07x slower                                                 |
| json                       | 2.75 ms                                                | 2.96 ms: 1.08x slower                                                  |
| fannkuch                   | 240 ms                                                 | 259 ms: 1.08x slower                                                   |
| aiohttp                    | 1.02 ms                                                | 1.11 ms: 1.09x slower                                                  |
| sqlglot_normalize          | 162 ms                                                 | 176 ms: 1.09x slower                                                   |
| xml_etree_process          | 33.6 ms                                                | 36.7 ms: 1.09x slower                                                  |
| nqueens                    | 55.9 ms                                                | 61.2 ms: 1.09x slower                                                  |
| pickle_list                | 2.70 us                                                | 2.96 us: 1.10x slower                                                  |
| json_loads                 | 15.3 us                                                | 17.0 us: 1.11x slower                                                  |
| scimark_sparse_mat_mult    | 2.81 ms                                                | 3.12 ms: 1.11x slower                                                  |
| unpickle                   | 8.29 us                                                | 9.25 us: 1.12x slower                                                  |
| regex_v8                   | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                  |
| unpickle_list              | 2.69 us                                                | 3.03 us: 1.13x slower                                                  |
| spectral_norm              | 65.7 ms                                                | 74.5 ms: 1.13x slower                                                  |
| sqlglot_optimize           | 29.6 ms                                                | 33.7 ms: 1.14x slower                                                  |
| nbody                      | 61.7 ms                                                | 70.2 ms: 1.14x slower                                                  |
| 2to3                       | 154 ms                                                 | 176 ms: 1.14x slower                                                   |
| regex_compile              | 72.8 ms                                                | 83.5 ms: 1.15x slower                                                  |
| tornado_http               | 69.1 ms                                                | 79.5 ms: 1.15x slower                                                  |
| scimark_fft                | 173 ms                                                 | 199 ms: 1.15x slower                                                   |
| genshi_xml                 | 28.5 ms                                                | 32.9 ms: 1.15x slower                                                  |
| pyflate                    | 284 ms                                                 | 328 ms: 1.16x slower                                                   |
| xml_etree_generate         | 45.8 ms                                                | 54.0 ms: 1.18x slower                                                  |
| scimark_lu                 | 67.7 ms                                                | 81.0 ms: 1.20x slower                                                  |
| bench_mp_pool              | 41.0 ms                                                | 51.2 ms: 1.25x slower                                                  |
| sqlite_synth               | 1.26 us                                                | 1.59 us: 1.27x slower                                                  |
| mypy2                      | 372 ms                                                 | 490 ms: 1.31x slower                                                   |
| scimark_sor                | 79.2 ms                                                | 107 ms: 1.35x slower                                                   |
| telco                      | 3.17 ms                                                | 4.55 ms: 1.44x slower                                                  |
| async_generators           | 192 ms                                                 | 301 ms: 1.57x slower                                                   |
| python_startup             | 10.8 ms                                                | 18.9 ms: 1.75x slower                                                  |
| python_startup_no_site     | 8.57 ms                                                | 17.1 ms: 1.99x slower                                                  |
| unpack_sequence            | 33.6 ns                                                | 113 ns: 3.35x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, deepcopy
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (8) of results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg


# HPT report

- Reliability score: 96.41% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.51x