# Results vs. 3.12.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: darwin-arm64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.235x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x slower
- Memory change: 0.54x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 249 ms: 1.47x slower                                                  |
| docutils       | 1.50 sec                                               | 1.76 sec: 1.17x slower                                                |
| tornado_http   | 69.3 ms                                                | 104 ms: 1.51x slower                                                  |
| Geometric mean | (ref)                                                  | 1.37x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 501 ms: 1.34x faster                                                  |
| async_tree_io              | 668 ms                                                 | 530 ms: 1.26x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 207 ms: 1.25x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 266 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 466 ms: 1.14x faster                                                  |
| async_tree_none            | 266 ms                                                 | 235 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 490 ms: 1.07x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 292 ms: 1.07x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| float          | 55.8 ms                                                | 93.0 ms: 1.67x slower                                                 |
| nbody          | 68.8 ms                                                | 154 ms: 2.24x slower                                                  |
| Geometric mean | (ref)                                                  | 1.55x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 146 ms: 1.06x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.51 ms: 1.05x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                 |
| regex_compile  | 77.9 ms                                                | 119 ms: 1.53x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle               | 7.23 us                                                | 7.03 us: 1.03x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 104 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 75.9 ms: 1.03x slower                                                 |
| pickle_dict          | 18.1 us                                                | 18.5 us: 1.03x slower                                                 |
| pickle_list          | 2.89 us                                                | 2.97 us: 1.03x slower                                                 |
| unpickle             | 9.12 us                                                | 9.46 us: 1.04x slower                                                 |
| json_loads           | 17.2 us                                                | 18.5 us: 1.07x slower                                                 |
| unpickle_list        | 3.02 us                                                | 3.26 us: 1.08x slower                                                 |
| xml_etree_generate   | 55.8 ms                                                | 67.9 ms: 1.22x slower                                                 |
| json_dumps           | 6.22 ms                                                | 7.91 ms: 1.27x slower                                                 |
| xml_etree_process    | 39.7 ms                                                | 56.3 ms: 1.42x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 1.99 sec: 1.43x slower                                                |
| pickle_pure_python   | 200 us                                                 | 346 us: 1.73x slower                                                  |
| unpickle_pure_python | 151 us                                                 | 262 us: 1.74x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.9 ms: 1.49x slower                                                 |
| python_startup         | 11.4 ms                                                | 17.4 ms: 1.52x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.50x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 36.1 ms: 1.62x slower                                                 |
| mako            | 7.71 ms                                                | 13.3 ms: 1.73x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.67x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| sqlglot_normalize          | 186 ms                                                 | 103 ms: 1.81x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 239 ms: 1.71x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 501 ms: 1.34x faster                                                  |
| async_tree_io              | 668 ms                                                 | 530 ms: 1.26x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 207 ms: 1.25x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 266 ms: 1.22x faster                                                  |
| gc_traversal               | 2.40 ms                                                | 2.05 ms: 1.17x faster                                                 |
| asyncio_tcp                | 449 ms                                                 | 385 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 466 ms: 1.14x faster                                                  |
| async_tree_none            | 266 ms                                                 | 235 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 490 ms: 1.07x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 292 ms: 1.07x faster                                                  |
| regex_dna                  | 154 ms                                                 | 146 ms: 1.06x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.51 ms: 1.05x faster                                                 |
| sqlite_synth               | 1.57 us                                                | 1.52 us: 1.03x faster                                                 |
| create_gc_cycles           | 701 us                                                 | 679 us: 1.03x faster                                                  |
| pickle                     | 7.23 us                                                | 7.03 us: 1.03x faster                                                 |
| xml_etree_parse            | 106 ms                                                 | 104 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.23 sec: 1.01x faster                                                |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 75.9 ms: 1.03x slower                                                 |
| pickle_dict                | 18.1 us                                                | 18.5 us: 1.03x slower                                                 |
| pickle_list                | 2.89 us                                                | 2.97 us: 1.03x slower                                                 |
| deepcopy                   | 235 us                                                 | 243 us: 1.04x slower                                                  |
| pathlib                    | 24.2 ms                                                | 25.1 ms: 1.04x slower                                                 |
| unpickle                   | 9.12 us                                                | 9.46 us: 1.04x slower                                                 |
| json_loads                 | 17.2 us                                                | 18.5 us: 1.07x slower                                                 |
| json                       | 3.09 ms                                                | 3.33 ms: 1.08x slower                                                 |
| unpickle_list              | 3.02 us                                                | 3.26 us: 1.08x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                 |
| async_generators           | 304 ms                                                 | 332 ms: 1.09x slower                                                  |
| deepcopy_memo              | 27.7 us                                                | 30.6 us: 1.11x slower                                                 |
| generators                 | 31.1 ms                                                | 35.0 ms: 1.13x slower                                                 |
| docutils                   | 1.50 sec                                               | 1.76 sec: 1.17x slower                                                |
| deepcopy_reduce            | 2.07 us                                                | 2.45 us: 1.18x slower                                                 |
| mdp                        | 1.58 sec                                               | 1.88 sec: 1.19x slower                                                |
| xml_etree_generate         | 55.8 ms                                                | 67.9 ms: 1.22x slower                                                 |
| nqueens                    | 62.4 ms                                                | 76.4 ms: 1.22x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 88.9 ms: 1.24x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 7.91 ms: 1.27x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 57.2 ms: 1.28x slower                                                 |
| coroutines                 | 19.2 ms                                                | 24.7 ms: 1.28x slower                                                 |
| comprehensions             | 14.5 us                                                | 18.7 us: 1.29x slower                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 4.07 ms: 1.30x slower                                                 |
| pycparser                  | 677 ms                                                 | 915 ms: 1.35x slower                                                  |
| scimark_fft                | 195 ms                                                 | 266 ms: 1.36x slower                                                  |
| dulwich_log                | 29.8 ms                                                | 40.9 ms: 1.37x slower                                                 |
| coverage                   | 38.9 ms                                                | 54.4 ms: 1.40x slower                                                 |
| xml_etree_process          | 39.7 ms                                                | 56.3 ms: 1.42x slower                                                 |
| fannkuch                   | 248 ms                                                 | 354 ms: 1.43x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.99 sec: 1.43x slower                                                |
| sympy_integrate            | 11.4 ms                                                | 16.3 ms: 1.43x slower                                                 |
| 2to3                       | 169 ms                                                 | 249 ms: 1.47x slower                                                  |
| telco                      | 3.68 ms                                                | 5.42 ms: 1.47x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 13.9 ms: 1.49x slower                                                 |
| crypto_pyaes               | 51.9 ms                                                | 77.8 ms: 1.50x slower                                                 |
| tornado_http               | 69.3 ms                                                | 104 ms: 1.51x slower                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 51.6 ms: 1.52x slower                                                 |
| python_startup             | 11.4 ms                                                | 17.4 ms: 1.52x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 142 us: 1.52x slower                                                  |
| regex_compile              | 77.9 ms                                                | 119 ms: 1.53x slower                                                  |
| pyflate                    | 316 ms                                                 | 490 ms: 1.55x slower                                                  |
| spectral_norm              | 76.4 ms                                                | 119 ms: 1.56x slower                                                  |
| sympy_str                  | 148 ms                                                 | 233 ms: 1.58x slower                                                  |
| bench_thread_pool          | 504 us                                                 | 798 us: 1.58x slower                                                  |
| django_template            | 22.3 ms                                                | 36.1 ms: 1.62x slower                                                 |
| pprint_safe_repr           | 497 ms                                                 | 810 ms: 1.63x slower                                                  |
| pprint_pformat             | 1.01 sec                                               | 1.65 sec: 1.63x slower                                                |
| logging_simple             | 3.69 us                                                | 6.10 us: 1.65x slower                                                 |
| logging_format             | 3.98 us                                                | 6.64 us: 1.67x slower                                                 |
| float                      | 55.8 ms                                                | 93.0 ms: 1.67x slower                                                 |
| hexiom                     | 4.54 ms                                                | 7.74 ms: 1.70x slower                                                 |
| mako                       | 7.71 ms                                                | 13.3 ms: 1.73x slower                                                 |
| pickle_pure_python         | 200 us                                                 | 346 us: 1.73x slower                                                  |
| richards                   | 32.1 ms                                                | 55.6 ms: 1.73x slower                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 78.4 ms: 1.74x slower                                                 |
| unpickle_pure_python       | 151 us                                                 | 262 us: 1.74x slower                                                  |
| chaos                      | 42.5 ms                                                | 74.7 ms: 1.76x slower                                                 |
| raytrace                   | 212 ms                                                 | 373 ms: 1.76x slower                                                  |
| sympy_expand               | 241 ms                                                 | 427 ms: 1.77x slower                                                  |
| logging_silent             | 76.4 ns                                                | 136 ns: 1.78x slower                                                  |
| go                         | 102 ms                                                 | 182 ms: 1.79x slower                                                  |
| richards_super             | 36.0 ms                                                | 64.7 ms: 1.80x slower                                                 |
| sympy_sum                  | 77.6 ms                                                | 141 ms: 1.81x slower                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.90 ms: 1.86x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 164 ms: 1.88x slower                                                  |
| scimark_lu                 | 76.0 ms                                                | 145 ms: 1.91x slower                                                  |
| sqlglot_parse              | 848 us                                                 | 1.65 ms: 1.95x slower                                                 |
| deltablue                  | 2.71 ms                                                | 5.61 ms: 2.07x slower                                                 |
| nbody                      | 68.8 ms                                                | 154 ms: 2.24x slower                                                  |
| unpack_sequence            | 31.5 ns                                                | 96.0 ns: 3.05x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.30x slower                                                          |
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20241005-3.14.0a0-16cd6cc-NOGIL/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.235x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.23x
- 95% likely to have a slowdown of 1.21x
- 99% likely to have a slowdown of 1.17x

# Memory
- memory change: 0.54x