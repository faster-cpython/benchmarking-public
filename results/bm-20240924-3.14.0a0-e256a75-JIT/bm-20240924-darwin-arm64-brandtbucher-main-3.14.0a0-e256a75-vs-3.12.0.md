# Results vs. 3.12.0

- fork: brandtbucher
- ref: main
- machine: darwin-arm64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.049x faster
- HPT reliability: 98.42%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.64x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 175 ms: 1.04x slower                                        |
| docutils       | 1.50 sec                                               | 1.55 sec: 1.03x slower                                      |
| tornado_http   | 69.3 ms                                                | 86.8 ms: 1.25x slower                                       |
| Geometric mean | (ref)                                                  | 1.10x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 186 ms: 1.38x faster                                        |
| async_tree_none            | 266 ms                                                 | 199 ms: 1.33x faster                                        |
| async_tree_memoization     | 312 ms                                                 | 247 ms: 1.26x faster                                        |
| async_tree_memoization_tg  | 323 ms                                                 | 256 ms: 1.26x faster                                        |
| async_tree_io_tg           | 669 ms                                                 | 554 ms: 1.21x faster                                        |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 459 ms: 1.16x faster                                        |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 459 ms: 1.14x faster                                        |
| async_tree_io              | 668 ms                                                 | 589 ms: 1.13x faster                                        |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.1 ms: 1.21x faster                                       |
| nbody          | 68.8 ms                                                | 63.5 ms: 1.08x faster                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.46 ms: 1.07x faster                                       |
| regex_dna      | 154 ms                                                 | 145 ms: 1.06x faster                                        |
| regex_compile  | 77.9 ms                                                | 75.6 ms: 1.03x faster                                       |
| regex_v8       | 16.0 ms                                                | 16.6 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| xml_etree_process    | 39.7 ms                                                | 34.0 ms: 1.17x faster                                       |
| unpickle_pure_python | 151 us                                                 | 131 us: 1.15x faster                                        |
| pickle_pure_python   | 200 us                                                 | 178 us: 1.12x faster                                        |
| xml_etree_generate   | 55.8 ms                                                | 49.7 ms: 1.12x faster                                       |
| tomli_loads          | 1.39 sec                                               | 1.25 sec: 1.12x faster                                      |
| unpickle_list        | 3.02 us                                                | 2.91 us: 1.04x faster                                       |
| xml_etree_iterparse  | 74.0 ms                                                | 71.6 ms: 1.03x faster                                       |
| json_loads           | 17.2 us                                                | 16.8 us: 1.02x faster                                       |
| xml_etree_parse      | 106 ms                                                 | 107 ms: 1.01x slower                                        |
| pickle_dict          | 18.1 us                                                | 18.3 us: 1.01x slower                                       |
| unpickle             | 9.12 us                                                | 9.22 us: 1.01x slower                                       |
| json_dumps           | 6.22 ms                                                | 6.31 ms: 1.01x slower                                       |
| pickle_list          | 2.89 us                                                | 2.94 us: 1.02x slower                                       |
| pickle               | 7.23 us                                                | 7.43 us: 1.03x slower                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 12.5 ms: 1.33x slower                                       |
| python_startup         | 11.4 ms                                                | 15.3 ms: 1.34x slower                                       |
| Geometric mean         | (ref)                                                  | 1.34x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| mako           | 7.71 ms                                                | 6.48 ms: 1.19x faster                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.3 us: 1.70x faster                                       |
| deepcopy                   | 235 us                                                 | 155 us: 1.51x faster                                        |
| async_tree_none_tg         | 258 ms                                                 | 186 ms: 1.38x faster                                        |
| deepcopy_reduce            | 2.07 us                                                | 1.52 us: 1.37x faster                                       |
| async_tree_none            | 266 ms                                                 | 199 ms: 1.33x faster                                        |
| generators                 | 31.1 ms                                                | 24.4 ms: 1.27x faster                                       |
| async_tree_memoization     | 312 ms                                                 | 247 ms: 1.26x faster                                        |
| async_tree_memoization_tg  | 323 ms                                                 | 256 ms: 1.26x faster                                        |
| logging_simple             | 3.69 us                                                | 2.97 us: 1.24x faster                                       |
| logging_silent             | 76.4 ns                                                | 62.0 ns: 1.23x faster                                       |
| raytrace                   | 212 ms                                                 | 173 ms: 1.22x faster                                        |
| logging_format             | 3.98 us                                                | 3.27 us: 1.22x faster                                       |
| float                      | 55.8 ms                                                | 46.1 ms: 1.21x faster                                       |
| async_tree_io_tg           | 669 ms                                                 | 554 ms: 1.21x faster                                        |
| coroutines                 | 19.2 ms                                                | 16.0 ms: 1.20x faster                                       |
| scimark_lu                 | 76.0 ms                                                | 63.7 ms: 1.19x faster                                       |
| mako                       | 7.71 ms                                                | 6.48 ms: 1.19x faster                                       |
| xml_etree_process          | 39.7 ms                                                | 34.0 ms: 1.17x faster                                       |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 459 ms: 1.16x faster                                        |
| deltablue                  | 2.71 ms                                                | 2.35 ms: 1.15x faster                                       |
| unpickle_pure_python       | 151 us                                                 | 131 us: 1.15x faster                                        |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 459 ms: 1.14x faster                                        |
| comprehensions             | 14.5 us                                                | 12.7 us: 1.14x faster                                       |
| spectral_norm              | 76.4 ms                                                | 67.0 ms: 1.14x faster                                       |
| async_tree_io              | 668 ms                                                 | 589 ms: 1.13x faster                                        |
| asyncio_tcp                | 449 ms                                                 | 397 ms: 1.13x faster                                        |
| pickle_pure_python         | 200 us                                                 | 178 us: 1.12x faster                                        |
| xml_etree_generate         | 55.8 ms                                                | 49.7 ms: 1.12x faster                                       |
| tomli_loads                | 1.39 sec                                               | 1.25 sec: 1.12x faster                                      |
| nbody                      | 68.8 ms                                                | 63.5 ms: 1.08x faster                                       |
| mdp                        | 1.58 sec                                               | 1.46 sec: 1.08x faster                                      |
| nqueens                    | 62.4 ms                                                | 57.7 ms: 1.08x faster                                       |
| regex_effbot               | 2.64 ms                                                | 2.46 ms: 1.07x faster                                       |
| bench_thread_pool          | 504 us                                                 | 471 us: 1.07x faster                                        |
| chaos                      | 42.5 ms                                                | 40.0 ms: 1.06x faster                                       |
| regex_dna                  | 154 ms                                                 | 145 ms: 1.06x faster                                        |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.98 ms: 1.05x faster                                       |
| json                       | 3.09 ms                                                | 2.94 ms: 1.05x faster                                       |
| scimark_fft                | 195 ms                                                 | 186 ms: 1.05x faster                                        |
| unpickle_list              | 3.02 us                                                | 2.91 us: 1.04x faster                                       |
| async_generators           | 304 ms                                                 | 293 ms: 1.04x faster                                        |
| xml_etree_iterparse        | 74.0 ms                                                | 71.6 ms: 1.03x faster                                       |
| regex_compile              | 77.9 ms                                                | 75.6 ms: 1.03x faster                                       |
| sympy_sum                  | 77.6 ms                                                | 75.4 ms: 1.03x faster                                       |
| dulwich_log                | 29.8 ms                                                | 29.0 ms: 1.03x faster                                       |
| sympy_str                  | 148 ms                                                 | 144 ms: 1.03x faster                                        |
| sqlglot_normalize          | 186 ms                                                 | 181 ms: 1.02x faster                                        |
| json_loads                 | 17.2 us                                                | 16.8 us: 1.02x faster                                       |
| pprint_safe_repr           | 497 ms                                                 | 495 ms: 1.00x faster                                        |
| sqlite_synth               | 1.57 us                                                | 1.57 us: 1.00x faster                                       |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                        |
| pprint_pformat             | 1.01 sec                                               | 1.01 sec: 1.00x slower                                      |
| crypto_pyaes               | 51.9 ms                                                | 52.1 ms: 1.00x slower                                       |
| scimark_sor                | 87.4 ms                                                | 87.8 ms: 1.01x slower                                       |
| xml_etree_parse            | 106 ms                                                 | 107 ms: 1.01x slower                                        |
| pickle_dict                | 18.1 us                                                | 18.3 us: 1.01x slower                                       |
| unpickle                   | 9.12 us                                                | 9.22 us: 1.01x slower                                       |
| json_dumps                 | 6.22 ms                                                | 6.31 ms: 1.01x slower                                       |
| sympy_integrate            | 11.4 ms                                                | 11.5 ms: 1.02x slower                                       |
| sqlglot_transpile          | 1.02 ms                                                | 1.04 ms: 1.02x slower                                       |
| go                         | 102 ms                                                 | 103 ms: 1.02x slower                                        |
| pickle_list                | 2.89 us                                                | 2.94 us: 1.02x slower                                       |
| gc_traversal               | 2.40 ms                                                | 2.45 ms: 1.02x slower                                       |
| typing_runtime_protocols   | 93.0 us                                                | 95.2 us: 1.02x slower                                       |
| sympy_expand               | 241 ms                                                 | 247 ms: 1.02x slower                                        |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.28 sec: 1.03x slower                                      |
| pickle                     | 7.23 us                                                | 7.43 us: 1.03x slower                                       |
| docutils                   | 1.50 sec                                               | 1.55 sec: 1.03x slower                                      |
| 2to3                       | 169 ms                                                 | 175 ms: 1.04x slower                                        |
| regex_v8                   | 16.0 ms                                                | 16.6 ms: 1.04x slower                                       |
| pyflate                    | 316 ms                                                 | 328 ms: 1.04x slower                                        |
| sqlglot_optimize           | 34.0 ms                                                | 35.5 ms: 1.04x slower                                       |
| hexiom                     | 4.54 ms                                                | 4.76 ms: 1.05x slower                                       |
| meteor_contest             | 71.7 ms                                                | 75.3 ms: 1.05x slower                                       |
| scimark_monte_carlo        | 45.0 ms                                                | 47.9 ms: 1.06x slower                                       |
| fannkuch                   | 248 ms                                                 | 265 ms: 1.07x slower                                        |
| bench_mp_pool              | 44.9 ms                                                | 50.9 ms: 1.13x slower                                       |
| coverage                   | 38.9 ms                                                | 44.4 ms: 1.14x slower                                       |
| tornado_http               | 69.3 ms                                                | 86.8 ms: 1.25x slower                                       |
| telco                      | 3.68 ms                                                | 4.72 ms: 1.28x slower                                       |
| create_gc_cycles           | 701 us                                                 | 902 us: 1.29x slower                                        |
| richards_super             | 36.0 ms                                                | 47.6 ms: 1.32x slower                                       |
| python_startup_no_site     | 9.37 ms                                                | 12.5 ms: 1.33x slower                                       |
| python_startup             | 11.4 ms                                                | 15.3 ms: 1.34x slower                                       |
| richards                   | 32.1 ms                                                | 44.4 ms: 1.38x slower                                       |
| unpack_sequence            | 31.5 ns                                                | 76.6 ns: 2.43x slower                                       |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                |

Benchmark hidden because not significant (5): pathlib, pidigits, django_template, sqlglot_parse, pycparser
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.049x faster
# HPT report

- Reliability score: 98.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.64x