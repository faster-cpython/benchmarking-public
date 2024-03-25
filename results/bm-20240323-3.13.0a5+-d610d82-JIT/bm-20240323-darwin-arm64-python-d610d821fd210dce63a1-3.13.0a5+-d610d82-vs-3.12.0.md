# Results vs. 3.12.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: darwin-arm64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.01x faster
- HPT reliability: 97.60%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.45x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 176 ms: 1.04x slower                                                   |
| chameleon      | 4.70 ms                                                | 4.41 ms: 1.06x faster                                                  |
| docutils       | 1.50 sec                                               | 1.54 sec: 1.02x slower                                                 |
| tornado_http   | 69.3 ms                                                | 79.5 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 242 ms: 1.33x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 207 ms: 1.24x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 254 ms: 1.23x faster                                                   |
| async_tree_none            | 266 ms                                                 | 221 ms: 1.20x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 449 ms: 1.19x faster                                                   |
| async_tree_io              | 668 ms                                                 | 567 ms: 1.18x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 574 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 455 ms: 1.15x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.2 ms: 1.13x faster                                                  |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                                   |
| nbody          | 68.8 ms                                                | 70.2 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 145 ms: 1.06x faster                                                   |
| regex_effbot   | 2.64 ms                                                | 2.55 ms: 1.03x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.9 ms: 1.06x slower                                                  |
| regex_compile  | 77.9 ms                                                | 83.5 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 183 us: 1.09x faster                                                   |
| tomli_loads          | 1.39 sec                                               | 1.28 sec: 1.09x faster                                                 |
| xml_etree_process    | 39.7 ms                                                | 36.7 ms: 1.08x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 98.8 ms: 1.08x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 142 us: 1.06x faster                                                   |
| xml_etree_iterparse  | 74.0 ms                                                | 70.0 ms: 1.06x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 54.0 ms: 1.03x faster                                                  |
| json_loads           | 17.2 us                                                | 17.0 us: 1.01x faster                                                  |
| pickle_dict          | 18.1 us                                                | 18.1 us: 1.00x slower                                                  |
| unpickle_list        | 3.02 us                                                | 3.03 us: 1.00x slower                                                  |
| unpickle             | 9.12 us                                                | 9.25 us: 1.01x slower                                                  |
| json_dumps           | 6.22 ms                                                | 6.35 ms: 1.02x slower                                                  |
| pickle_list          | 2.89 us                                                | 2.96 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 18.9 ms: 1.65x slower                                                  |
| python_startup_no_site | 9.37 ms                                                | 17.1 ms: 1.82x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.74x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.89 ms: 1.12x faster                                                  |
| django_template | 22.3 ms                                                | 20.8 ms: 1.08x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 242 ms: 1.33x faster                                                   |
| typing_runtime_protocols   | 93.0 us                                                | 69.8 us: 1.33x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 207 ms: 1.24x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 254 ms: 1.23x faster                                                   |
| comprehensions             | 14.5 us                                                | 12.0 us: 1.21x faster                                                  |
| async_tree_none            | 266 ms                                                 | 221 ms: 1.20x faster                                                   |
| raytrace                   | 212 ms                                                 | 178 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 449 ms: 1.19x faster                                                   |
| async_tree_io              | 668 ms                                                 | 567 ms: 1.18x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 574 ms: 1.17x faster                                                   |
| logging_silent             | 76.4 ns                                                | 65.6 ns: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 455 ms: 1.15x faster                                                   |
| generators                 | 31.1 ms                                                | 27.1 ms: 1.15x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.36 ms: 1.14x faster                                                  |
| deepcopy_memo              | 27.7 us                                                | 24.2 us: 1.14x faster                                                  |
| float                      | 55.8 ms                                                | 49.2 ms: 1.13x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.26 us: 1.13x faster                                                  |
| logging_format             | 3.98 us                                                | 3.54 us: 1.13x faster                                                  |
| mako                       | 7.71 ms                                                | 6.89 ms: 1.12x faster                                                  |
| chaos                      | 42.5 ms                                                | 38.1 ms: 1.12x faster                                                  |
| coroutines                 | 19.2 ms                                                | 17.2 ms: 1.12x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.86 us: 1.12x faster                                                  |
| crypto_pyaes               | 51.9 ms                                                | 46.9 ms: 1.11x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 768 us: 1.10x faster                                                   |
| asyncio_tcp                | 449 ms                                                 | 410 ms: 1.09x faster                                                   |
| pickle_pure_python         | 200 us                                                 | 183 us: 1.09x faster                                                   |
| deepcopy                   | 235 us                                                 | 215 us: 1.09x faster                                                   |
| sqlglot_transpile          | 1.02 ms                                                | 938 us: 1.09x faster                                                   |
| tomli_loads                | 1.39 sec                                               | 1.28 sec: 1.09x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 36.7 ms: 1.08x faster                                                  |
| xml_etree_parse            | 106 ms                                                 | 98.8 ms: 1.08x faster                                                  |
| django_template            | 22.3 ms                                                | 20.8 ms: 1.08x faster                                                  |
| chameleon                  | 4.70 ms                                                | 4.41 ms: 1.06x faster                                                  |
| regex_dna                  | 154 ms                                                 | 145 ms: 1.06x faster                                                   |
| unpickle_pure_python       | 151 us                                                 | 142 us: 1.06x faster                                                   |
| xml_etree_iterparse        | 74.0 ms                                                | 70.0 ms: 1.06x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 176 ms: 1.06x faster                                                   |
| sympy_str                  | 148 ms                                                 | 140 ms: 1.06x faster                                                   |
| json                       | 3.09 ms                                                | 2.96 ms: 1.04x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.55 ms: 1.03x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 54.0 ms: 1.03x faster                                                  |
| richards_super             | 36.0 ms                                                | 35.0 ms: 1.03x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 491 us: 1.03x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 74.5 ms: 1.03x faster                                                  |
| richards                   | 32.1 ms                                                | 31.4 ms: 1.02x faster                                                  |
| sympy_expand               | 241 ms                                                 | 236 ms: 1.02x faster                                                   |
| sympy_sum                  | 77.6 ms                                                | 76.0 ms: 1.02x faster                                                  |
| nqueens                    | 62.4 ms                                                | 61.2 ms: 1.02x faster                                                  |
| json_loads                 | 17.2 us                                                | 17.0 us: 1.01x faster                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 44.5 ms: 1.01x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 11.2 ms: 1.01x faster                                                  |
| async_generators           | 304 ms                                                 | 301 ms: 1.01x faster                                                   |
| pycparser                  | 677 ms                                                 | 670 ms: 1.01x faster                                                   |
| sqlglot_optimize           | 34.0 ms                                                | 33.7 ms: 1.01x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.57 sec: 1.01x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 29.6 ms: 1.01x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.12 ms: 1.00x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                   |
| pidigits                   | 282 ms                                                 | 282 ms: 1.00x slower                                                   |
| pickle_dict                | 18.1 us                                                | 18.1 us: 1.00x slower                                                  |
| unpickle_list              | 3.02 us                                                | 3.03 us: 1.00x slower                                                  |
| pprint_pformat             | 1.01 sec                                               | 1.02 sec: 1.01x slower                                                 |
| sqlite_synth               | 1.57 us                                                | 1.59 us: 1.01x slower                                                  |
| unpickle                   | 9.12 us                                                | 9.25 us: 1.01x slower                                                  |
| pathlib                    | 24.2 ms                                                | 24.6 ms: 1.02x slower                                                  |
| scimark_fft                | 195 ms                                                 | 199 ms: 1.02x slower                                                   |
| nbody                      | 68.8 ms                                                | 70.2 ms: 1.02x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 6.35 ms: 1.02x slower                                                  |
| meteor_contest             | 71.7 ms                                                | 73.3 ms: 1.02x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.54 sec: 1.02x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 719 us: 1.03x slower                                                   |
| pickle_list                | 2.89 us                                                | 2.96 us: 1.03x slower                                                  |
| go                         | 102 ms                                                 | 105 ms: 1.03x slower                                                   |
| 2to3                       | 169 ms                                                 | 176 ms: 1.04x slower                                                   |
| pyflate                    | 316 ms                                                 | 328 ms: 1.04x slower                                                   |
| fannkuch                   | 248 ms                                                 | 259 ms: 1.04x slower                                                   |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.31 sec: 1.05x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 16.9 ms: 1.06x slower                                                  |
| scimark_lu                 | 76.0 ms                                                | 81.0 ms: 1.07x slower                                                  |
| hexiom                     | 4.54 ms                                                | 4.86 ms: 1.07x slower                                                  |
| regex_compile              | 77.9 ms                                                | 83.5 ms: 1.07x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 51.2 ms: 1.14x slower                                                  |
| tornado_http               | 69.3 ms                                                | 79.5 ms: 1.15x slower                                                  |
| coverage                   | 38.9 ms                                                | 46.5 ms: 1.20x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 107 ms: 1.23x slower                                                   |
| telco                      | 3.68 ms                                                | 4.55 ms: 1.24x slower                                                  |
| mypy2                      | 380 ms                                                 | 490 ms: 1.29x slower                                                   |
| python_startup             | 11.4 ms                                                | 18.9 ms: 1.65x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 17.1 ms: 1.82x slower                                                  |
| unpack_sequence            | 31.5 ns                                                | 113 ns: 3.59x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (6): pickle, pprint_safe_repr, gc_traversal, gunicorn, dask, aiohttp
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 97.60% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.45x