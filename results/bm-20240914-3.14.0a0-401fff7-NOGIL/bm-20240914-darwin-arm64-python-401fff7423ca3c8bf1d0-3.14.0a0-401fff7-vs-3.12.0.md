# Results vs. 3.12.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: darwin-arm64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.253x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x slower
- Memory change: 0.65x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 249 ms: 1.47x slower                                                  |
| docutils       | 1.50 sec                                               | 1.78 sec: 1.18x slower                                                |
| tornado_http   | 69.3 ms                                                | 103 ms: 1.48x slower                                                  |
| Geometric mean | (ref)                                                  | 1.37x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 515 ms: 1.30x faster                                                  |
| async_tree_io              | 668 ms                                                 | 541 ms: 1.23x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 213 ms: 1.21x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 271 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 467 ms: 1.14x faster                                                  |
| async_tree_none            | 266 ms                                                 | 239 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 494 ms: 1.06x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 296 ms: 1.06x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| float          | 55.8 ms                                                | 97.7 ms: 1.75x slower                                                 |
| nbody          | 68.8 ms                                                | 157 ms: 2.29x slower                                                  |
| Geometric mean | (ref)                                                  | 1.59x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 139 ms: 1.11x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.45 ms: 1.08x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.2 ms: 1.08x slower                                                 |
| regex_compile  | 77.9 ms                                                | 121 ms: 1.56x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle               | 7.23 us                                                | 7.01 us: 1.03x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 105 ms: 1.02x faster                                                  |
| pickle_dict          | 18.1 us                                                | 18.4 us: 1.02x slower                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 77.1 ms: 1.04x slower                                                 |
| unpickle_list        | 3.02 us                                                | 3.22 us: 1.07x slower                                                 |
| unpickle             | 9.12 us                                                | 9.84 us: 1.08x slower                                                 |
| json_loads           | 17.2 us                                                | 19.2 us: 1.12x slower                                                 |
| xml_etree_generate   | 55.8 ms                                                | 70.1 ms: 1.25x slower                                                 |
| json_dumps           | 6.22 ms                                                | 7.92 ms: 1.27x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 2.03 sec: 1.46x slower                                                |
| xml_etree_process    | 39.7 ms                                                | 58.3 ms: 1.47x slower                                                 |
| pickle_pure_python   | 200 us                                                 | 348 us: 1.74x slower                                                  |
| unpickle_pure_python | 151 us                                                 | 265 us: 1.76x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.21x slower                                                          |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 15.6 ms: 1.66x slower                                                 |
| python_startup         | 11.4 ms                                                | 19.2 ms: 1.68x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.67x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 35.9 ms: 1.61x slower                                                 |
| mako            | 7.71 ms                                                | 13.5 ms: 1.74x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.68x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| sqlglot_normalize          | 186 ms                                                 | 105 ms: 1.77x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 515 ms: 1.30x faster                                                  |
| asyncio_tcp                | 449 ms                                                 | 353 ms: 1.27x faster                                                  |
| async_tree_io              | 668 ms                                                 | 541 ms: 1.23x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 213 ms: 1.21x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 271 ms: 1.19x faster                                                  |
| gc_traversal               | 2.40 ms                                                | 2.06 ms: 1.17x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 467 ms: 1.14x faster                                                  |
| regex_dna                  | 154 ms                                                 | 139 ms: 1.11x faster                                                  |
| async_tree_none            | 266 ms                                                 | 239 ms: 1.11x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.45 ms: 1.08x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 494 ms: 1.06x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 296 ms: 1.06x faster                                                  |
| pickle                     | 7.23 us                                                | 7.01 us: 1.03x faster                                                 |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                                 |
| xml_etree_parse            | 106 ms                                                 | 105 ms: 1.02x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 405 ms: 1.01x faster                                                  |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| create_gc_cycles           | 701 us                                                 | 699 us: 1.00x faster                                                  |
| pickle_dict                | 18.1 us                                                | 18.4 us: 1.02x slower                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 77.1 ms: 1.04x slower                                                 |
| deepcopy                   | 235 us                                                 | 249 us: 1.06x slower                                                  |
| unpickle_list              | 3.02 us                                                | 3.22 us: 1.07x slower                                                 |
| unpickle                   | 9.12 us                                                | 9.84 us: 1.08x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.2 ms: 1.08x slower                                                 |
| async_generators           | 304 ms                                                 | 332 ms: 1.09x slower                                                  |
| pathlib                    | 24.2 ms                                                | 26.7 ms: 1.10x slower                                                 |
| json                       | 3.09 ms                                                | 3.41 ms: 1.11x slower                                                 |
| json_loads                 | 17.2 us                                                | 19.2 us: 1.12x slower                                                 |
| generators                 | 31.1 ms                                                | 35.0 ms: 1.13x slower                                                 |
| deepcopy_memo              | 27.7 us                                                | 31.6 us: 1.14x slower                                                 |
| mdp                        | 1.58 sec                                               | 1.84 sec: 1.16x slower                                                |
| docutils                   | 1.50 sec                                               | 1.78 sec: 1.18x slower                                                |
| deepcopy_reduce            | 2.07 us                                                | 2.49 us: 1.20x slower                                                 |
| nqueens                    | 62.4 ms                                                | 76.1 ms: 1.22x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 89.5 ms: 1.25x slower                                                 |
| xml_etree_generate         | 55.8 ms                                                | 70.1 ms: 1.25x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 56.8 ms: 1.27x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 7.92 ms: 1.27x slower                                                 |
| comprehensions             | 14.5 us                                                | 18.9 us: 1.30x slower                                                 |
| coroutines                 | 19.2 ms                                                | 25.1 ms: 1.30x slower                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 4.19 ms: 1.34x slower                                                 |
| sympy_integrate            | 11.4 ms                                                | 15.7 ms: 1.38x slower                                                 |
| pycparser                  | 677 ms                                                 | 935 ms: 1.38x slower                                                  |
| dulwich_log                | 29.8 ms                                                | 41.2 ms: 1.38x slower                                                 |
| scimark_fft                | 195 ms                                                 | 274 ms: 1.40x slower                                                  |
| fannkuch                   | 248 ms                                                 | 358 ms: 1.44x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 2.03 sec: 1.46x slower                                                |
| coverage                   | 38.9 ms                                                | 56.9 ms: 1.47x slower                                                 |
| xml_etree_process          | 39.7 ms                                                | 58.3 ms: 1.47x slower                                                 |
| 2to3                       | 169 ms                                                 | 249 ms: 1.47x slower                                                  |
| tornado_http               | 69.3 ms                                                | 103 ms: 1.48x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 77.8 ms: 1.50x slower                                                 |
| pyflate                    | 316 ms                                                 | 484 ms: 1.54x slower                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 52.4 ms: 1.54x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 144 us: 1.55x slower                                                  |
| regex_compile              | 77.9 ms                                                | 121 ms: 1.56x slower                                                  |
| spectral_norm              | 76.4 ms                                                | 120 ms: 1.57x slower                                                  |
| bench_thread_pool          | 504 us                                                 | 798 us: 1.58x slower                                                  |
| sympy_str                  | 148 ms                                                 | 234 ms: 1.58x slower                                                  |
| telco                      | 3.68 ms                                                | 5.90 ms: 1.60x slower                                                 |
| django_template            | 22.3 ms                                                | 35.9 ms: 1.61x slower                                                 |
| pprint_pformat             | 1.01 sec                                               | 1.66 sec: 1.64x slower                                                |
| pprint_safe_repr           | 497 ms                                                 | 817 ms: 1.64x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 15.6 ms: 1.66x slower                                                 |
| logging_simple             | 3.69 us                                                | 6.17 us: 1.67x slower                                                 |
| python_startup             | 11.4 ms                                                | 19.2 ms: 1.68x slower                                                 |
| logging_format             | 3.98 us                                                | 6.73 us: 1.69x slower                                                 |
| hexiom                     | 4.54 ms                                                | 7.77 ms: 1.71x slower                                                 |
| pickle_pure_python         | 200 us                                                 | 348 us: 1.74x slower                                                  |
| mako                       | 7.71 ms                                                | 13.5 ms: 1.74x slower                                                 |
| float                      | 55.8 ms                                                | 97.7 ms: 1.75x slower                                                 |
| unpickle_pure_python       | 151 us                                                 | 265 us: 1.76x slower                                                  |
| richards                   | 32.1 ms                                                | 57.0 ms: 1.77x slower                                                 |
| chaos                      | 42.5 ms                                                | 76.0 ms: 1.79x slower                                                 |
| sympy_expand               | 241 ms                                                 | 432 ms: 1.79x slower                                                  |
| logging_silent             | 76.4 ns                                                | 137 ns: 1.80x slower                                                  |
| raytrace                   | 212 ms                                                 | 381 ms: 1.80x slower                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 81.1 ms: 1.80x slower                                                 |
| sympy_sum                  | 77.6 ms                                                | 140 ms: 1.80x slower                                                  |
| go                         | 102 ms                                                 | 184 ms: 1.82x slower                                                  |
| richards_super             | 36.0 ms                                                | 65.7 ms: 1.82x slower                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.94 ms: 1.90x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 167 ms: 1.92x slower                                                  |
| sqlglot_parse              | 848 us                                                 | 1.69 ms: 2.00x slower                                                 |
| scimark_lu                 | 76.0 ms                                                | 152 ms: 2.00x slower                                                  |
| deltablue                  | 2.71 ms                                                | 5.74 ms: 2.12x slower                                                 |
| nbody                      | 68.8 ms                                                | 157 ms: 2.29x slower                                                  |
| unpack_sequence            | 31.5 ns                                                | 97.9 ns: 3.11x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.32x slower                                                          |

Benchmark hidden because not significant (2): pickle_list, asyncio_tcp_ssl
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20240914-3.14.0a0-401fff7-NOGIL/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.253x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.25x
- 95% likely to have a slowdown of 1.22x
- 99% likely to have a slowdown of 1.18x

# Memory
- memory change: 0.65x