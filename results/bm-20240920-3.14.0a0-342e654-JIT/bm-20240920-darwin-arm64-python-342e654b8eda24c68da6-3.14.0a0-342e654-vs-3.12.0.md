# Results vs. 3.12.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: darwin-arm64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.04x faster
- HPT reliability: 98.29%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.63x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 176 ms: 1.04x slower                                                  |
| docutils       | 1.50 sec                                               | 1.56 sec: 1.04x slower                                                |
| tornado_http   | 69.3 ms                                                | 84.5 ms: 1.22x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 186 ms: 1.38x faster                                                  |
| async_tree_none            | 266 ms                                                 | 201 ms: 1.32x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 247 ms: 1.26x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 257 ms: 1.26x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 541 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 461 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 459 ms: 1.14x faster                                                  |
| async_tree_io              | 668 ms                                                 | 589 ms: 1.13x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.1 ms: 1.21x faster                                                 |
| nbody          | 68.8 ms                                                | 63.6 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.49 ms: 1.06x faster                                                 |
| regex_compile  | 77.9 ms                                                | 74.3 ms: 1.05x faster                                                 |
| regex_dna      | 154 ms                                                 | 148 ms: 1.04x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 39.7 ms                                                | 34.1 ms: 1.16x faster                                                 |
| unpickle_pure_python | 151 us                                                 | 131 us: 1.15x faster                                                  |
| pickle_pure_python   | 200 us                                                 | 178 us: 1.12x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.25 sec: 1.11x faster                                                |
| xml_etree_generate   | 55.8 ms                                                | 50.1 ms: 1.11x faster                                                 |
| unpickle_list        | 3.02 us                                                | 2.88 us: 1.05x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 72.3 ms: 1.02x faster                                                 |
| json_loads           | 17.2 us                                                | 16.9 us: 1.02x faster                                                 |
| json_dumps           | 6.22 ms                                                | 6.19 ms: 1.00x faster                                                 |
| pickle_list          | 2.89 us                                                | 2.92 us: 1.01x slower                                                 |
| unpickle             | 9.12 us                                                | 9.23 us: 1.01x slower                                                 |
| pickle_dict          | 18.1 us                                                | 18.3 us: 1.01x slower                                                 |
| pickle               | 7.23 us                                                | 7.42 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 11.5 ms: 1.23x slower                                                 |
| python_startup         | 11.4 ms                                                | 14.4 ms: 1.27x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.25x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.45 ms: 1.19x faster                                                 |
| django_template | 22.3 ms                                                | 22.6 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.1 us: 1.72x faster                                                 |
| deepcopy                   | 235 us                                                 | 153 us: 1.53x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 186 ms: 1.38x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.51 us: 1.37x faster                                                 |
| async_tree_none            | 266 ms                                                 | 201 ms: 1.32x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 247 ms: 1.26x faster                                                  |
| generators                 | 31.1 ms                                                | 24.6 ms: 1.26x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 257 ms: 1.26x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 541 ms: 1.24x faster                                                  |
| raytrace                   | 212 ms                                                 | 173 ms: 1.23x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.02 us: 1.22x faster                                                 |
| logging_silent             | 76.4 ns                                                | 62.8 ns: 1.22x faster                                                 |
| float                      | 55.8 ms                                                | 46.1 ms: 1.21x faster                                                 |
| logging_format             | 3.98 us                                                | 3.31 us: 1.20x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.0 ms: 1.20x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 63.4 ms: 1.20x faster                                                 |
| mako                       | 7.71 ms                                                | 6.45 ms: 1.19x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 34.1 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 461 ms: 1.16x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.35 ms: 1.15x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 131 us: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 459 ms: 1.14x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 67.0 ms: 1.14x faster                                                 |
| async_tree_io              | 668 ms                                                 | 589 ms: 1.13x faster                                                  |
| comprehensions             | 14.5 us                                                | 12.8 us: 1.13x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 178 us: 1.12x faster                                                  |
| tomli_loads                | 1.39 sec                                               | 1.25 sec: 1.11x faster                                                |
| xml_etree_generate         | 55.8 ms                                                | 50.1 ms: 1.11x faster                                                 |
| asyncio_tcp                | 449 ms                                                 | 412 ms: 1.09x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.46 sec: 1.09x faster                                                |
| nbody                      | 68.8 ms                                                | 63.6 ms: 1.08x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 469 us: 1.07x faster                                                  |
| nqueens                    | 62.4 ms                                                | 58.2 ms: 1.07x faster                                                 |
| scimark_fft                | 195 ms                                                 | 184 ms: 1.06x faster                                                  |
| json                       | 3.09 ms                                                | 2.91 ms: 1.06x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.49 ms: 1.06x faster                                                 |
| chaos                      | 42.5 ms                                                | 40.1 ms: 1.06x faster                                                 |
| pathlib                    | 24.2 ms                                                | 22.9 ms: 1.06x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.98 ms: 1.05x faster                                                 |
| async_generators           | 304 ms                                                 | 290 ms: 1.05x faster                                                  |
| regex_compile              | 77.9 ms                                                | 74.3 ms: 1.05x faster                                                 |
| unpickle_list              | 3.02 us                                                | 2.88 us: 1.05x faster                                                 |
| regex_dna                  | 154 ms                                                 | 148 ms: 1.04x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 75.2 ms: 1.03x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 29.0 ms: 1.03x faster                                                 |
| sympy_str                  | 148 ms                                                 | 143 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 72.3 ms: 1.02x faster                                                 |
| json_loads                 | 17.2 us                                                | 16.9 us: 1.02x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 183 ms: 1.02x faster                                                  |
| json_dumps                 | 6.22 ms                                                | 6.19 ms: 1.00x faster                                                 |
| go                         | 102 ms                                                 | 101 ms: 1.00x faster                                                  |
| crypto_pyaes               | 51.9 ms                                                | 51.7 ms: 1.00x faster                                                 |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                  |
| scimark_sor                | 87.4 ms                                                | 87.7 ms: 1.00x slower                                                 |
| sqlite_synth               | 1.57 us                                                | 1.58 us: 1.01x slower                                                 |
| pickle_list                | 2.89 us                                                | 2.92 us: 1.01x slower                                                 |
| django_template            | 22.3 ms                                                | 22.6 ms: 1.01x slower                                                 |
| unpickle                   | 9.12 us                                                | 9.23 us: 1.01x slower                                                 |
| pickle_dict                | 18.1 us                                                | 18.3 us: 1.01x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 94.3 us: 1.01x slower                                                 |
| sympy_integrate            | 11.4 ms                                                | 11.5 ms: 1.01x slower                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.04 ms: 1.01x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.45 ms: 1.02x slower                                                 |
| pprint_safe_repr           | 497 ms                                                 | 509 ms: 1.02x slower                                                  |
| sympy_expand               | 241 ms                                                 | 247 ms: 1.02x slower                                                  |
| pickle                     | 7.23 us                                                | 7.42 us: 1.03x slower                                                 |
| pprint_pformat             | 1.01 sec                                               | 1.04 sec: 1.03x slower                                                |
| pyflate                    | 316 ms                                                 | 326 ms: 1.03x slower                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.03x slower                                                |
| regex_v8                   | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                 |
| 2to3                       | 169 ms                                                 | 176 ms: 1.04x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.56 sec: 1.04x slower                                                |
| hexiom                     | 4.54 ms                                                | 4.74 ms: 1.04x slower                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 35.5 ms: 1.04x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 75.2 ms: 1.05x slower                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 47.4 ms: 1.05x slower                                                 |
| fannkuch                   | 248 ms                                                 | 263 ms: 1.06x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 49.4 ms: 1.10x slower                                                 |
| coverage                   | 38.9 ms                                                | 44.8 ms: 1.15x slower                                                 |
| tornado_http               | 69.3 ms                                                | 84.5 ms: 1.22x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 11.5 ms: 1.23x slower                                                 |
| python_startup             | 11.4 ms                                                | 14.4 ms: 1.27x slower                                                 |
| richards_super             | 36.0 ms                                                | 46.4 ms: 1.29x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 904 us: 1.29x slower                                                  |
| telco                      | 3.68 ms                                                | 4.80 ms: 1.30x slower                                                 |
| richards                   | 32.1 ms                                                | 44.4 ms: 1.38x slower                                                 |
| unpack_sequence            | 31.5 ns                                                | 75.9 ns: 2.41x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (4): pidigits, pycparser, sqlglot_parse, xml_etree_parse
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.63x