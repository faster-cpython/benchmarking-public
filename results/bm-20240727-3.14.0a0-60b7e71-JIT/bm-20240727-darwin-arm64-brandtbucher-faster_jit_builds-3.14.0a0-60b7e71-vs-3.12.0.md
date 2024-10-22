# Results vs. 3.12.0

- fork: brandtbucher
- ref: faster_jit_builds
- machine: darwin-arm64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.52x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 176 ms: 1.04x slower                                                     |
| docutils       | 1.50 sec                                               | 1.57 sec: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 226 ms: 1.43x faster                                                     |
| async_tree_none_tg         | 258 ms                                                 | 182 ms: 1.41x faster                                                     |
| async_tree_none            | 266 ms                                                 | 195 ms: 1.36x faster                                                     |
| async_tree_io_tg           | 669 ms                                                 | 507 ms: 1.32x faster                                                     |
| async_tree_memoization     | 312 ms                                                 | 240 ms: 1.30x faster                                                     |
| async_tree_io              | 668 ms                                                 | 547 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 443 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 453 ms: 1.16x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.30x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 45.9 ms: 1.21x faster                                                    |
| nbody          | 68.8 ms                                                | 63.0 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                  | 1.10x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 73.4 ms: 1.06x faster                                                    |
| regex_dna      | 154 ms                                                 | 150 ms: 1.03x faster                                                     |
| regex_effbot   | 2.64 ms                                                | 2.73 ms: 1.03x slower                                                    |
| regex_v8       | 16.0 ms                                                | 17.3 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 173 us: 1.15x faster                                                     |
| unpickle_pure_python | 151 us                                                 | 133 us: 1.13x faster                                                     |
| xml_etree_process    | 39.7 ms                                                | 35.4 ms: 1.12x faster                                                    |
| tomli_loads          | 1.39 sec                                               | 1.24 sec: 1.12x faster                                                   |
| xml_etree_generate   | 55.8 ms                                                | 51.7 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 74.0 ms                                                | 72.7 ms: 1.02x faster                                                    |
| json_loads           | 17.2 us                                                | 17.0 us: 1.02x faster                                                    |
| json_dumps           | 6.22 ms                                                | 6.19 ms: 1.00x faster                                                    |
| xml_etree_parse      | 106 ms                                                 | 109 ms: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 17.1 ms: 1.50x slower                                                    |
| python_startup_no_site | 9.37 ms                                                | 14.3 ms: 1.53x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.51x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.43 ms: 1.20x faster                                                    |
| django_template | 22.3 ms                                                | 21.3 ms: 1.05x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.6 us: 1.67x faster                                                    |
| deepcopy                   | 235 us                                                 | 154 us: 1.53x faster                                                     |
| generators                 | 31.1 ms                                                | 21.6 ms: 1.44x faster                                                    |
| async_tree_memoization_tg  | 323 ms                                                 | 226 ms: 1.43x faster                                                     |
| async_tree_none_tg         | 258 ms                                                 | 182 ms: 1.41x faster                                                     |
| async_tree_none            | 266 ms                                                 | 195 ms: 1.36x faster                                                     |
| deepcopy_reduce            | 2.07 us                                                | 1.54 us: 1.34x faster                                                    |
| raytrace                   | 212 ms                                                 | 160 ms: 1.32x faster                                                     |
| async_tree_io_tg           | 669 ms                                                 | 507 ms: 1.32x faster                                                     |
| async_tree_memoization     | 312 ms                                                 | 240 ms: 1.30x faster                                                     |
| logging_silent             | 76.4 ns                                                | 61.4 ns: 1.25x faster                                                    |
| logging_simple             | 3.69 us                                                | 3.00 us: 1.23x faster                                                    |
| async_tree_io              | 668 ms                                                 | 547 ms: 1.22x faster                                                     |
| float                      | 55.8 ms                                                | 45.9 ms: 1.21x faster                                                    |
| logging_format             | 3.98 us                                                | 3.29 us: 1.21x faster                                                    |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 443 ms: 1.20x faster                                                     |
| mako                       | 7.71 ms                                                | 6.43 ms: 1.20x faster                                                    |
| deltablue                  | 2.71 ms                                                | 2.28 ms: 1.19x faster                                                    |
| comprehensions             | 14.5 us                                                | 12.3 us: 1.18x faster                                                    |
| coroutines                 | 19.2 ms                                                | 16.3 ms: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 453 ms: 1.16x faster                                                     |
| pickle_pure_python         | 200 us                                                 | 173 us: 1.15x faster                                                     |
| spectral_norm              | 76.4 ms                                                | 67.1 ms: 1.14x faster                                                    |
| unpickle_pure_python       | 151 us                                                 | 133 us: 1.13x faster                                                     |
| xml_etree_process          | 39.7 ms                                                | 35.4 ms: 1.12x faster                                                    |
| tomli_loads                | 1.39 sec                                               | 1.24 sec: 1.12x faster                                                   |
| chaos                      | 42.5 ms                                                | 38.5 ms: 1.10x faster                                                    |
| asyncio_tcp                | 449 ms                                                 | 408 ms: 1.10x faster                                                     |
| mdp                        | 1.58 sec                                               | 1.44 sec: 1.10x faster                                                   |
| nbody                      | 68.8 ms                                                | 63.0 ms: 1.09x faster                                                    |
| nqueens                    | 62.4 ms                                                | 57.1 ms: 1.09x faster                                                    |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.89 ms: 1.08x faster                                                    |
| xml_etree_generate         | 55.8 ms                                                | 51.7 ms: 1.08x faster                                                    |
| bench_thread_pool          | 504 us                                                 | 470 us: 1.07x faster                                                     |
| scimark_fft                | 195 ms                                                 | 182 ms: 1.07x faster                                                     |
| json                       | 3.09 ms                                                | 2.89 ms: 1.07x faster                                                    |
| sqlglot_normalize          | 186 ms                                                 | 175 ms: 1.06x faster                                                     |
| regex_compile              | 77.9 ms                                                | 73.4 ms: 1.06x faster                                                    |
| richards                   | 32.1 ms                                                | 30.4 ms: 1.06x faster                                                    |
| sympy_str                  | 148 ms                                                 | 140 ms: 1.06x faster                                                     |
| sympy_sum                  | 77.6 ms                                                | 73.4 ms: 1.06x faster                                                    |
| async_generators           | 304 ms                                                 | 289 ms: 1.05x faster                                                     |
| dulwich_log                | 29.8 ms                                                | 28.5 ms: 1.05x faster                                                    |
| django_template            | 22.3 ms                                                | 21.3 ms: 1.05x faster                                                    |
| richards_super             | 36.0 ms                                                | 34.6 ms: 1.04x faster                                                    |
| hexiom                     | 4.54 ms                                                | 4.36 ms: 1.04x faster                                                    |
| sqlglot_optimize           | 34.0 ms                                                | 32.8 ms: 1.04x faster                                                    |
| regex_dna                  | 154 ms                                                 | 150 ms: 1.03x faster                                                     |
| pathlib                    | 24.2 ms                                                | 23.6 ms: 1.03x faster                                                    |
| scimark_monte_carlo        | 45.0 ms                                                | 43.9 ms: 1.03x faster                                                    |
| pprint_safe_repr           | 497 ms                                                 | 487 ms: 1.02x faster                                                     |
| xml_etree_iterparse        | 74.0 ms                                                | 72.7 ms: 1.02x faster                                                    |
| sqlglot_transpile          | 1.02 ms                                                | 1.00 ms: 1.02x faster                                                    |
| json_loads                 | 17.2 us                                                | 17.0 us: 1.02x faster                                                    |
| sympy_integrate            | 11.4 ms                                                | 11.2 ms: 1.02x faster                                                    |
| sqlglot_parse              | 848 us                                                 | 835 us: 1.02x faster                                                     |
| pyflate                    | 316 ms                                                 | 311 ms: 1.02x faster                                                     |
| meteor_contest             | 71.7 ms                                                | 70.9 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.01 sec                                               | 1.00 sec: 1.01x faster                                                   |
| go                         | 102 ms                                                 | 101 ms: 1.01x faster                                                     |
| json_dumps                 | 6.22 ms                                                | 6.19 ms: 1.00x faster                                                    |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                     |
| typing_runtime_protocols   | 93.0 us                                                | 93.8 us: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.27 sec: 1.02x slower                                                   |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.03x slower                                                    |
| xml_etree_parse            | 106 ms                                                 | 109 ms: 1.03x slower                                                     |
| regex_effbot               | 2.64 ms                                                | 2.73 ms: 1.03x slower                                                    |
| 2to3                       | 169 ms                                                 | 176 ms: 1.04x slower                                                     |
| docutils                   | 1.50 sec                                               | 1.57 sec: 1.04x slower                                                   |
| pycparser                  | 677 ms                                                 | 708 ms: 1.05x slower                                                     |
| dask                       | 222 ms                                                 | 234 ms: 1.05x slower                                                     |
| scimark_lu                 | 76.0 ms                                                | 80.2 ms: 1.06x slower                                                    |
| regex_v8                   | 16.0 ms                                                | 17.3 ms: 1.09x slower                                                    |
| bench_mp_pool              | 44.9 ms                                                | 51.4 ms: 1.15x slower                                                    |
| scimark_sor                | 87.4 ms                                                | 101 ms: 1.15x slower                                                     |
| coverage                   | 38.9 ms                                                | 46.0 ms: 1.18x slower                                                    |
| telco                      | 3.68 ms                                                | 4.51 ms: 1.22x slower                                                    |
| create_gc_cycles           | 701 us                                                 | 903 us: 1.29x slower                                                     |
| python_startup             | 11.4 ms                                                | 17.1 ms: 1.50x slower                                                    |
| python_startup_no_site     | 9.37 ms                                                | 14.3 ms: 1.53x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                             |

Benchmark hidden because not significant (5): tornado_http, fannkuch, crypto_pyaes, pidigits, sympy_expand
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240727-3.14.0a0-60b7e71-JIT/bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.52x