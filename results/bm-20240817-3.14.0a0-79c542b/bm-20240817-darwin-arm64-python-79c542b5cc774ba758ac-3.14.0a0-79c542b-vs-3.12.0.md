# Results vs. 3.12.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: darwin-arm64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.48x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 162 ms: 1.05x faster                                                  |
| docutils       | 1.50 sec                                               | 1.47 sec: 1.02x faster                                                |
| tornado_http   | 69.3 ms                                                | 86.5 ms: 1.25x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 182 ms: 1.42x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 228 ms: 1.41x faster                                                  |
| async_tree_none            | 266 ms                                                 | 192 ms: 1.39x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 505 ms: 1.32x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 241 ms: 1.30x faster                                                  |
| async_tree_io              | 668 ms                                                 | 539 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 438 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 453 ms: 1.16x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.7 ms: 1.15x faster                                                 |
| nbody          | 68.8 ms                                                | 60.8 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.0 ms: 1.15x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.47 ms: 1.07x faster                                                 |
| regex_dna      | 154 ms                                                 | 145 ms: 1.06x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 182 us: 1.10x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 37.3 ms: 1.06x faster                                                 |
| unpickle_pure_python | 151 us                                                 | 143 us: 1.05x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 53.1 ms: 1.05x faster                                                 |
| json_loads           | 17.2 us                                                | 17.3 us: 1.00x slower                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 74.8 ms: 1.01x slower                                                 |
| json_dumps           | 6.22 ms                                                | 6.38 ms: 1.03x slower                                                 |
| xml_etree_parse      | 106 ms                                                 | 111 ms: 1.05x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.48 sec: 1.06x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 10.9 ms: 1.16x slower                                                 |
| python_startup         | 11.4 ms                                                | 13.8 ms: 1.21x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.6 ms: 1.14x faster                                                 |
| mako            | 7.71 ms                                                | 6.96 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 17.1 us: 1.62x faster                                                 |
| deepcopy                   | 235 us                                                 | 146 us: 1.61x faster                                                  |
| generators                 | 31.1 ms                                                | 20.3 ms: 1.53x faster                                                 |
| comprehensions             | 14.5 us                                                | 10.0 us: 1.45x faster                                                 |
| raytrace                   | 212 ms                                                 | 147 ms: 1.44x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 182 ms: 1.42x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 228 ms: 1.41x faster                                                  |
| async_tree_none            | 266 ms                                                 | 192 ms: 1.39x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.51 us: 1.37x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 505 ms: 1.32x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 241 ms: 1.30x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.11 ms: 1.28x faster                                                 |
| logging_silent             | 76.4 ns                                                | 60.4 ns: 1.27x faster                                                 |
| async_tree_io              | 668 ms                                                 | 539 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 438 ms: 1.21x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.07 us: 1.20x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.2 ms: 1.19x faster                                                 |
| chaos                      | 42.5 ms                                                | 35.8 ms: 1.19x faster                                                 |
| logging_format             | 3.98 us                                                | 3.40 us: 1.17x faster                                                 |
| nqueens                    | 62.4 ms                                                | 53.3 ms: 1.17x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 453 ms: 1.16x faster                                                  |
| float                      | 55.8 ms                                                | 48.7 ms: 1.15x faster                                                 |
| regex_compile              | 77.9 ms                                                | 68.0 ms: 1.15x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 744 us: 1.14x faster                                                  |
| django_template            | 22.3 ms                                                | 19.6 ms: 1.14x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 67.2 ms: 1.14x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 902 us: 1.13x faster                                                  |
| nbody                      | 68.8 ms                                                | 60.8 ms: 1.13x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 67.8 ms: 1.12x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 450 us: 1.12x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.81 ms: 1.12x faster                                                 |
| hexiom                     | 4.54 ms                                                | 4.10 ms: 1.11x faster                                                 |
| mako                       | 7.71 ms                                                | 6.96 ms: 1.11x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 26.9 ms: 1.11x faster                                                 |
| sympy_str                  | 148 ms                                                 | 134 ms: 1.10x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 168 ms: 1.10x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 70.4 ms: 1.10x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 182 us: 1.10x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 31.3 ms: 1.09x faster                                                 |
| sympy_integrate            | 11.4 ms                                                | 10.5 ms: 1.09x faster                                                 |
| asyncio_tcp                | 449 ms                                                 | 413 ms: 1.09x faster                                                  |
| richards_super             | 36.0 ms                                                | 33.3 ms: 1.08x faster                                                 |
| async_generators           | 304 ms                                                 | 282 ms: 1.08x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.47 ms: 1.07x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 466 ms: 1.07x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 37.3 ms: 1.06x faster                                                 |
| pprint_pformat             | 1.01 sec                                               | 952 ms: 1.06x faster                                                  |
| regex_dna                  | 154 ms                                                 | 145 ms: 1.06x faster                                                  |
| richards                   | 32.1 ms                                                | 30.3 ms: 1.06x faster                                                 |
| pycparser                  | 677 ms                                                 | 638 ms: 1.06x faster                                                  |
| sympy_expand               | 241 ms                                                 | 228 ms: 1.06x faster                                                  |
| scimark_fft                | 195 ms                                                 | 185 ms: 1.05x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 143 us: 1.05x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 53.1 ms: 1.05x faster                                                 |
| go                         | 102 ms                                                 | 96.6 ms: 1.05x faster                                                 |
| 2to3                       | 169 ms                                                 | 162 ms: 1.05x faster                                                  |
| json                       | 3.09 ms                                                | 2.98 ms: 1.04x faster                                                 |
| pathlib                    | 24.2 ms                                                | 23.4 ms: 1.04x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 43.5 ms: 1.03x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.54 sec: 1.03x faster                                                |
| docutils                   | 1.50 sec                                               | 1.47 sec: 1.02x faster                                                |
| crypto_pyaes               | 51.9 ms                                                | 50.7 ms: 1.02x faster                                                 |
| meteor_contest             | 71.7 ms                                                | 71.9 ms: 1.00x slower                                                 |
| json_loads                 | 17.2 us                                                | 17.3 us: 1.00x slower                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 74.8 ms: 1.01x slower                                                 |
| pyflate                    | 316 ms                                                 | 321 ms: 1.02x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.45 ms: 1.02x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.38 ms: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.28 sec: 1.03x slower                                                |
| bench_mp_pool              | 44.9 ms                                                | 46.5 ms: 1.04x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                 |
| xml_etree_parse            | 106 ms                                                 | 111 ms: 1.05x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.48 sec: 1.06x slower                                                |
| fannkuch                   | 248 ms                                                 | 265 ms: 1.07x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 93.8 ms: 1.07x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 10.9 ms: 1.16x slower                                                 |
| coverage                   | 38.9 ms                                                | 45.4 ms: 1.17x slower                                                 |
| python_startup             | 11.4 ms                                                | 13.8 ms: 1.21x slower                                                 |
| telco                      | 3.68 ms                                                | 4.58 ms: 1.24x slower                                                 |
| tornado_http               | 69.3 ms                                                | 86.5 ms: 1.25x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 895 us: 1.28x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, pidigits, typing_runtime_protocols
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240817-3.14.0a0-79c542b/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.48x