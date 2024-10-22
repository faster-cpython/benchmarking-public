# Results vs. 3.12.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: darwin-arm64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.05x faster
- HPT reliability: 94.42%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.67x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 179 ms: 1.06x slower                                                  |
| docutils       | 1.50 sec                                               | 1.62 sec: 1.08x slower                                                |
| tornado_http   | 69.3 ms                                                | 81.0 ms: 1.17x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 182 ms: 1.42x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 229 ms: 1.41x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 492 ms: 1.36x faster                                                  |
| async_tree_none            | 266 ms                                                 | 197 ms: 1.35x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 242 ms: 1.29x faster                                                  |
| async_tree_io              | 668 ms                                                 | 543 ms: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 444 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 456 ms: 1.15x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.6 ms: 1.20x faster                                                 |
| nbody          | 68.8 ms                                                | 63.8 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_dna      | 154 ms                                                 | 145 ms: 1.07x faster                                                  |
| regex_compile  | 77.9 ms                                                | 74.8 ms: 1.04x faster                                                 |
| regex_v8       | 16.0 ms                                                | 16.9 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 39.7 ms                                                | 34.4 ms: 1.15x faster                                                 |
| unpickle_pure_python | 151 us                                                 | 134 us: 1.12x faster                                                  |
| pickle_pure_python   | 200 us                                                 | 179 us: 1.12x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 50.3 ms: 1.11x faster                                                 |
| tomli_loads          | 1.39 sec                                               | 1.26 sec: 1.10x faster                                                |
| xml_etree_iterparse  | 74.0 ms                                                | 71.7 ms: 1.03x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 109 ms: 1.02x slower                                                  |
| json_dumps           | 6.22 ms                                                | 6.50 ms: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 11.6 ms: 1.24x slower                                                 |
| python_startup         | 11.4 ms                                                | 14.3 ms: 1.25x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.24x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.50 ms: 1.19x faster                                                 |
| django_template | 22.3 ms                                                | 23.0 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.2 us: 1.71x faster                                                 |
| deepcopy                   | 235 us                                                 | 155 us: 1.52x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 182 ms: 1.42x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 229 ms: 1.41x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.51 us: 1.38x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 492 ms: 1.36x faster                                                  |
| async_tree_none            | 266 ms                                                 | 197 ms: 1.35x faster                                                  |
| raytrace                   | 212 ms                                                 | 164 ms: 1.29x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 242 ms: 1.29x faster                                                  |
| generators                 | 31.1 ms                                                | 24.5 ms: 1.27x faster                                                 |
| logging_silent             | 76.4 ns                                                | 62.1 ns: 1.23x faster                                                 |
| async_tree_io              | 668 ms                                                 | 543 ms: 1.23x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.02 us: 1.22x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 444 ms: 1.20x faster                                                  |
| float                      | 55.8 ms                                                | 46.6 ms: 1.20x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.20x faster                                                 |
| logging_format             | 3.98 us                                                | 3.33 us: 1.19x faster                                                 |
| mako                       | 7.71 ms                                                | 6.50 ms: 1.19x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.32 ms: 1.17x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 65.6 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 456 ms: 1.15x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 34.4 ms: 1.15x faster                                                 |
| comprehensions             | 14.5 us                                                | 12.7 us: 1.15x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 134 us: 1.12x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 179 us: 1.12x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 50.3 ms: 1.11x faster                                                 |
| tomli_loads                | 1.39 sec                                               | 1.26 sec: 1.10x faster                                                |
| spectral_norm              | 76.4 ms                                                | 69.7 ms: 1.10x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.45 sec: 1.09x faster                                                |
| nbody                      | 68.8 ms                                                | 63.8 ms: 1.08x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 469 us: 1.08x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_dna                  | 154 ms                                                 | 145 ms: 1.07x faster                                                  |
| chaos                      | 42.5 ms                                                | 40.1 ms: 1.06x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 28.2 ms: 1.06x faster                                                 |
| json                       | 3.09 ms                                                | 2.92 ms: 1.06x faster                                                 |
| nqueens                    | 62.4 ms                                                | 59.2 ms: 1.05x faster                                                 |
| regex_compile              | 77.9 ms                                                | 74.8 ms: 1.04x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 71.7 ms: 1.03x faster                                                 |
| pathlib                    | 24.2 ms                                                | 23.5 ms: 1.03x faster                                                 |
| async_generators           | 304 ms                                                 | 297 ms: 1.02x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.08 ms: 1.02x faster                                                 |
| scimark_fft                | 195 ms                                                 | 194 ms: 1.01x faster                                                  |
| sympy_str                  | 148 ms                                                 | 147 ms: 1.00x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 77.3 ms: 1.00x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 185 ms: 1.00x faster                                                  |
| crypto_pyaes               | 51.9 ms                                                | 52.1 ms: 1.00x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 88.0 ms: 1.01x slower                                                 |
| sqlglot_parse              | 848 us                                                 | 856 us: 1.01x slower                                                  |
| xml_etree_parse            | 106 ms                                                 | 109 ms: 1.02x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.03x slower                                                 |
| pycparser                  | 677 ms                                                 | 695 ms: 1.03x slower                                                  |
| pprint_safe_repr           | 497 ms                                                 | 512 ms: 1.03x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 95.8 us: 1.03x slower                                                 |
| django_template            | 22.3 ms                                                | 23.0 ms: 1.03x slower                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.05 ms: 1.03x slower                                                 |
| pyflate                    | 316 ms                                                 | 327 ms: 1.04x slower                                                  |
| pprint_pformat             | 1.01 sec                                               | 1.05 sec: 1.04x slower                                                |
| hexiom                     | 4.54 ms                                                | 4.72 ms: 1.04x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 74.6 ms: 1.04x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                                |
| sympy_expand               | 241 ms                                                 | 252 ms: 1.04x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 6.50 ms: 1.04x slower                                                 |
| sympy_integrate            | 11.4 ms                                                | 11.9 ms: 1.05x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 16.9 ms: 1.06x slower                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 36.0 ms: 1.06x slower                                                 |
| 2to3                       | 169 ms                                                 | 179 ms: 1.06x slower                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 48.0 ms: 1.07x slower                                                 |
| docutils                   | 1.50 sec                                               | 1.62 sec: 1.08x slower                                                |
| fannkuch                   | 248 ms                                                 | 269 ms: 1.08x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 49.1 ms: 1.10x slower                                                 |
| coverage                   | 38.9 ms                                                | 44.6 ms: 1.15x slower                                                 |
| tornado_http               | 69.3 ms                                                | 81.0 ms: 1.17x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 11.6 ms: 1.24x slower                                                 |
| python_startup             | 11.4 ms                                                | 14.3 ms: 1.25x slower                                                 |
| telco                      | 3.68 ms                                                | 4.64 ms: 1.26x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 893 us: 1.27x slower                                                  |
| richards_super             | 36.0 ms                                                | 48.1 ms: 1.34x slower                                                 |
| richards                   | 32.1 ms                                                | 45.9 ms: 1.43x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (5): json_loads, asyncio_websockets, asyncio_tcp, pidigits, go
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240817-3.14.0a0-79c542b-JIT/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 94.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.67x