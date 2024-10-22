# Results vs. 3.12.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: darwin-arm64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.56x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 164 ms: 1.03x faster                                                  |
| docutils       | 1.50 sec                                               | 1.49 sec: 1.01x faster                                                |
| tornado_http   | 69.3 ms                                                | 66.8 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 228 ms: 1.42x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 183 ms: 1.41x faster                                                  |
| async_tree_none            | 266 ms                                                 | 195 ms: 1.36x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 509 ms: 1.31x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 240 ms: 1.30x faster                                                  |
| async_tree_io              | 668 ms                                                 | 547 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 443 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 453 ms: 1.16x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 68.8 ms                                                | 59.6 ms: 1.15x faster                                                 |
| float          | 55.8 ms                                                | 48.4 ms: 1.15x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.4 ms: 1.14x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.55 ms: 1.03x faster                                                 |
| regex_dna      | 154 ms                                                 | 150 ms: 1.03x faster                                                  |
| regex_v8       | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 184 us: 1.09x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 143 us: 1.05x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 53.4 ms: 1.05x faster                                                 |
| xml_etree_process    | 39.7 ms                                                | 37.9 ms: 1.05x faster                                                 |
| json_loads           | 17.2 us                                                | 17.2 us: 1.00x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 111 ms: 1.04x slower                                                  |
| json_dumps           | 6.22 ms                                                | 6.54 ms: 1.05x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 1.48 sec: 1.06x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 15.4 ms: 1.35x slower                                                 |
| python_startup_no_site | 9.37 ms                                                | 12.8 ms: 1.36x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.36x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.9 ms: 1.12x faster                                                 |
| mako            | 7.71 ms                                                | 7.02 ms: 1.10x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.9 us: 1.63x faster                                                 |
| deepcopy                   | 235 us                                                 | 145 us: 1.62x faster                                                  |
| generators                 | 31.1 ms                                                | 20.6 ms: 1.51x faster                                                 |
| raytrace                   | 212 ms                                                 | 148 ms: 1.43x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 228 ms: 1.42x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 183 ms: 1.41x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.50 us: 1.38x faster                                                 |
| async_tree_none            | 266 ms                                                 | 195 ms: 1.36x faster                                                  |
| comprehensions             | 14.5 us                                                | 10.9 us: 1.33x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 509 ms: 1.31x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 240 ms: 1.30x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.12 ms: 1.28x faster                                                 |
| logging_silent             | 76.4 ns                                                | 60.0 ns: 1.27x faster                                                 |
| async_tree_io              | 668 ms                                                 | 547 ms: 1.22x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.05 us: 1.21x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 443 ms: 1.20x faster                                                  |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.19x faster                                                 |
| chaos                      | 42.5 ms                                                | 36.0 ms: 1.18x faster                                                 |
| logging_format             | 3.98 us                                                | 3.38 us: 1.18x faster                                                 |
| nqueens                    | 62.4 ms                                                | 53.3 ms: 1.17x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 453 ms: 1.16x faster                                                  |
| nbody                      | 68.8 ms                                                | 59.6 ms: 1.15x faster                                                 |
| float                      | 55.8 ms                                                | 48.4 ms: 1.15x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 66.8 ms: 1.14x faster                                                 |
| regex_compile              | 77.9 ms                                                | 68.4 ms: 1.14x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 67.0 ms: 1.13x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 748 us: 1.13x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.77 ms: 1.13x faster                                                 |
| hexiom                     | 4.54 ms                                                | 4.06 ms: 1.12x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 911 us: 1.12x faster                                                  |
| django_template            | 22.3 ms                                                | 19.9 ms: 1.12x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 452 us: 1.11x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.42 sec: 1.11x faster                                                |
| asyncio_tcp                | 449 ms                                                 | 405 ms: 1.11x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 27.1 ms: 1.10x faster                                                 |
| mako                       | 7.71 ms                                                | 7.02 ms: 1.10x faster                                                 |
| sympy_str                  | 148 ms                                                 | 135 ms: 1.10x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 71.0 ms: 1.09x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 184 us: 1.09x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 171 ms: 1.09x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 10.5 ms: 1.08x faster                                                 |
| async_generators           | 304 ms                                                 | 280 ms: 1.08x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 31.6 ms: 1.08x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 470 ms: 1.06x faster                                                  |
| scimark_fft                | 195 ms                                                 | 185 ms: 1.06x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 958 ms: 1.05x faster                                                  |
| pycparser                  | 677 ms                                                 | 642 ms: 1.05x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 143 us: 1.05x faster                                                  |
| pathlib                    | 24.2 ms                                                | 23.1 ms: 1.05x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 53.4 ms: 1.05x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 37.9 ms: 1.05x faster                                                 |
| json                       | 3.09 ms                                                | 2.96 ms: 1.04x faster                                                 |
| richards_super             | 36.0 ms                                                | 34.6 ms: 1.04x faster                                                 |
| sympy_expand               | 241 ms                                                 | 232 ms: 1.04x faster                                                  |
| go                         | 102 ms                                                 | 97.7 ms: 1.04x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 43.3 ms: 1.04x faster                                                 |
| tornado_http               | 69.3 ms                                                | 66.8 ms: 1.04x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.55 ms: 1.03x faster                                                 |
| 2to3                       | 169 ms                                                 | 164 ms: 1.03x faster                                                  |
| regex_dna                  | 154 ms                                                 | 150 ms: 1.03x faster                                                  |
| crypto_pyaes               | 51.9 ms                                                | 50.4 ms: 1.03x faster                                                 |
| richards                   | 32.1 ms                                                | 31.6 ms: 1.02x faster                                                 |
| docutils                   | 1.50 sec                                               | 1.49 sec: 1.01x faster                                                |
| json_loads                 | 17.2 us                                                | 17.2 us: 1.00x faster                                                 |
| meteor_contest             | 71.7 ms                                                | 72.1 ms: 1.00x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 94.2 us: 1.01x slower                                                 |
| pyflate                    | 316 ms                                                 | 321 ms: 1.02x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.03x slower                                                 |
| dask                       | 222 ms                                                 | 230 ms: 1.03x slower                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                                |
| xml_etree_parse            | 106 ms                                                 | 111 ms: 1.04x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 6.54 ms: 1.05x slower                                                 |
| fannkuch                   | 248 ms                                                 | 263 ms: 1.06x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.48 sec: 1.06x slower                                                |
| scimark_sor                | 87.4 ms                                                | 93.2 ms: 1.07x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 48.3 ms: 1.08x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                 |
| coverage                   | 38.9 ms                                                | 44.3 ms: 1.14x slower                                                 |
| telco                      | 3.68 ms                                                | 4.60 ms: 1.25x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 878 us: 1.25x slower                                                  |
| python_startup             | 11.4 ms                                                | 15.4 ms: 1.35x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 12.8 ms: 1.36x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, pidigits, xml_etree_iterparse
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.56x