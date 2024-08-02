# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b2
- machine: darwin-arm64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 173 ms: 1.02x slower                                       |
| chameleon      | 4.70 ms                                                | 4.41 ms: 1.06x faster                                      |
| docutils       | 1.50 sec                                               | 1.51 sec: 1.01x slower                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 242 ms: 1.33x faster                                       |
| async_tree_none_tg         | 258 ms                                                 | 200 ms: 1.28x faster                                       |
| async_tree_none            | 266 ms                                                 | 212 ms: 1.25x faster                                       |
| async_tree_memoization     | 312 ms                                                 | 263 ms: 1.19x faster                                       |
| async_tree_io_tg           | 669 ms                                                 | 570 ms: 1.17x faster                                       |
| async_tree_io              | 668 ms                                                 | 571 ms: 1.17x faster                                       |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 456 ms: 1.17x faster                                       |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 472 ms: 1.11x faster                                       |
| Geometric mean             | (ref)                                                  | 1.21x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.4 ms: 1.18x faster                                      |
| nbody          | 68.8 ms                                                | 63.5 ms: 1.08x faster                                      |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 71.9 ms: 1.08x faster                                      |
| regex_dna      | 154 ms                                                 | 149 ms: 1.03x faster                                       |
| regex_effbot   | 2.64 ms                                                | 2.58 ms: 1.02x faster                                      |
| regex_v8       | 16.0 ms                                                | 17.3 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 173 us: 1.15x faster                                       |
| unpickle_pure_python | 151 us                                                 | 132 us: 1.14x faster                                       |
| tomli_loads          | 1.39 sec                                               | 1.24 sec: 1.12x faster                                     |
| xml_etree_process    | 39.7 ms                                                | 35.8 ms: 1.11x faster                                      |
| xml_etree_generate   | 55.8 ms                                                | 51.6 ms: 1.08x faster                                      |
| unpickle_list        | 3.02 us                                                | 2.88 us: 1.05x faster                                      |
| xml_etree_iterparse  | 74.0 ms                                                | 70.5 ms: 1.05x faster                                      |
| json_loads           | 17.2 us                                                | 16.9 us: 1.02x faster                                      |
| xml_etree_parse      | 106 ms                                                 | 105 ms: 1.01x faster                                       |
| json_dumps           | 6.22 ms                                                | 6.17 ms: 1.01x faster                                      |
| unpickle             | 9.12 us                                                | 9.19 us: 1.01x slower                                      |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                      |
| pickle_list          | 2.89 us                                                | 2.99 us: 1.03x slower                                      |
| pickle               | 7.23 us                                                | 7.52 us: 1.04x slower                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 16.4 ms: 1.43x slower                                      |
| python_startup_no_site | 9.37 ms                                                | 13.4 ms: 1.43x slower                                      |
| Geometric mean         | (ref)                                                  | 1.43x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.40 ms: 1.21x faster                                      |
| django_template | 22.3 ms                                                | 21.3 ms: 1.05x faster                                      |
| Geometric mean  | (ref)                                                  | 1.12x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 242 ms: 1.33x faster                                       |
| generators                 | 31.1 ms                                                | 23.6 ms: 1.32x faster                                      |
| raytrace                   | 212 ms                                                 | 163 ms: 1.30x faster                                       |
| deepcopy_memo              | 27.7 us                                                | 21.5 us: 1.29x faster                                      |
| async_tree_none_tg         | 258 ms                                                 | 200 ms: 1.28x faster                                       |
| async_tree_none            | 266 ms                                                 | 212 ms: 1.25x faster                                       |
| logging_simple             | 3.69 us                                                | 3.02 us: 1.22x faster                                      |
| logging_silent             | 76.4 ns                                                | 63.1 ns: 1.21x faster                                      |
| mako                       | 7.71 ms                                                | 6.40 ms: 1.21x faster                                      |
| coroutines                 | 19.2 ms                                                | 16.0 ms: 1.20x faster                                      |
| logging_format             | 3.98 us                                                | 3.33 us: 1.20x faster                                      |
| comprehensions             | 14.5 us                                                | 12.2 us: 1.19x faster                                      |
| async_tree_memoization     | 312 ms                                                 | 263 ms: 1.19x faster                                       |
| float                      | 55.8 ms                                                | 47.4 ms: 1.18x faster                                      |
| async_tree_io_tg           | 669 ms                                                 | 570 ms: 1.17x faster                                       |
| async_tree_io              | 668 ms                                                 | 571 ms: 1.17x faster                                       |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 456 ms: 1.17x faster                                       |
| pickle_pure_python         | 200 us                                                 | 173 us: 1.15x faster                                       |
| unpickle_pure_python       | 151 us                                                 | 132 us: 1.14x faster                                       |
| deepcopy_reduce            | 2.07 us                                                | 1.82 us: 1.14x faster                                      |
| spectral_norm              | 76.4 ms                                                | 67.5 ms: 1.13x faster                                      |
| deepcopy                   | 235 us                                                 | 208 us: 1.13x faster                                       |
| tomli_loads                | 1.39 sec                                               | 1.24 sec: 1.12x faster                                     |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 472 ms: 1.11x faster                                       |
| xml_etree_process          | 39.7 ms                                                | 35.8 ms: 1.11x faster                                      |
| mdp                        | 1.58 sec                                               | 1.43 sec: 1.11x faster                                     |
| nqueens                    | 62.4 ms                                                | 56.8 ms: 1.10x faster                                      |
| deltablue                  | 2.71 ms                                                | 2.47 ms: 1.10x faster                                      |
| chaos                      | 42.5 ms                                                | 38.9 ms: 1.09x faster                                      |
| nbody                      | 68.8 ms                                                | 63.5 ms: 1.08x faster                                      |
| regex_compile              | 77.9 ms                                                | 71.9 ms: 1.08x faster                                      |
| xml_etree_generate         | 55.8 ms                                                | 51.6 ms: 1.08x faster                                      |
| sympy_str                  | 148 ms                                                 | 137 ms: 1.08x faster                                       |
| asyncio_tcp                | 449 ms                                                 | 417 ms: 1.08x faster                                       |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.92 ms: 1.07x faster                                      |
| sympy_sum                  | 77.6 ms                                                | 72.4 ms: 1.07x faster                                      |
| pprint_safe_repr           | 497 ms                                                 | 464 ms: 1.07x faster                                       |
| fannkuch                   | 248 ms                                                 | 233 ms: 1.07x faster                                       |
| chameleon                  | 4.70 ms                                                | 4.41 ms: 1.06x faster                                      |
| pprint_pformat             | 1.01 sec                                               | 958 ms: 1.06x faster                                       |
| scimark_fft                | 195 ms                                                 | 185 ms: 1.05x faster                                       |
| json                       | 3.09 ms                                                | 2.93 ms: 1.05x faster                                      |
| unpickle_list              | 3.02 us                                                | 2.88 us: 1.05x faster                                      |
| xml_etree_iterparse        | 74.0 ms                                                | 70.5 ms: 1.05x faster                                      |
| bench_thread_pool          | 504 us                                                 | 481 us: 1.05x faster                                       |
| django_template            | 22.3 ms                                                | 21.3 ms: 1.05x faster                                      |
| sqlglot_optimize           | 34.0 ms                                                | 32.6 ms: 1.04x faster                                      |
| sympy_integrate            | 11.4 ms                                                | 10.9 ms: 1.04x faster                                      |
| hexiom                     | 4.54 ms                                                | 4.36 ms: 1.04x faster                                      |
| dulwich_log                | 29.8 ms                                                | 28.8 ms: 1.04x faster                                      |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.03x faster                                       |
| pathlib                    | 24.2 ms                                                | 23.4 ms: 1.03x faster                                      |
| sqlglot_parse              | 848 us                                                 | 826 us: 1.03x faster                                       |
| async_generators           | 304 ms                                                 | 296 ms: 1.03x faster                                       |
| scimark_monte_carlo        | 45.0 ms                                                | 44.0 ms: 1.02x faster                                      |
| sympy_expand               | 241 ms                                                 | 236 ms: 1.02x faster                                       |
| regex_effbot               | 2.64 ms                                                | 2.58 ms: 1.02x faster                                      |
| sqlglot_transpile          | 1.02 ms                                                | 1.00 ms: 1.02x faster                                      |
| json_loads                 | 17.2 us                                                | 16.9 us: 1.02x faster                                      |
| richards                   | 32.1 ms                                                | 31.7 ms: 1.01x faster                                      |
| xml_etree_parse            | 106 ms                                                 | 105 ms: 1.01x faster                                       |
| richards_super             | 36.0 ms                                                | 35.7 ms: 1.01x faster                                      |
| json_dumps                 | 6.22 ms                                                | 6.17 ms: 1.01x faster                                      |
| pycparser                  | 677 ms                                                 | 672 ms: 1.01x faster                                       |
| meteor_contest             | 71.7 ms                                                | 71.4 ms: 1.00x faster                                      |
| pidigits                   | 282 ms                                                 | 282 ms: 1.00x slower                                       |
| go                         | 102 ms                                                 | 102 ms: 1.00x slower                                       |
| unpickle                   | 9.12 us                                                | 9.19 us: 1.01x slower                                      |
| docutils                   | 1.50 sec                                               | 1.51 sec: 1.01x slower                                     |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                      |
| aiohttp                    | 1.08 ms                                                | 1.10 ms: 1.02x slower                                      |
| 2to3                       | 169 ms                                                 | 173 ms: 1.02x slower                                       |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.03x slower                                      |
| pickle_list                | 2.89 us                                                | 2.99 us: 1.03x slower                                      |
| scimark_lu                 | 76.0 ms                                                | 78.6 ms: 1.04x slower                                      |
| pickle                     | 7.23 us                                                | 7.52 us: 1.04x slower                                      |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.30 sec: 1.04x slower                                     |
| mypy2                      | 380 ms                                                 | 408 ms: 1.07x slower                                       |
| regex_v8                   | 16.0 ms                                                | 17.3 ms: 1.08x slower                                      |
| bench_mp_pool              | 44.9 ms                                                | 51.4 ms: 1.15x slower                                      |
| scimark_sor                | 87.4 ms                                                | 100 ms: 1.15x slower                                       |
| coverage                   | 38.9 ms                                                | 44.9 ms: 1.16x slower                                      |
| telco                      | 3.68 ms                                                | 4.64 ms: 1.26x slower                                      |
| create_gc_cycles           | 701 us                                                 | 903 us: 1.29x slower                                       |
| python_startup             | 11.4 ms                                                | 16.4 ms: 1.43x slower                                      |
| python_startup_no_site     | 9.37 ms                                                | 13.4 ms: 1.43x slower                                      |
| Geometric mean             | (ref)                                                  | 1.05x faster                                               |

Benchmark hidden because not significant (8): tornado_http, crypto_pyaes, sqlite_synth, pyflate, asyncio_websockets, gunicorn, typing_runtime_protocols, dask
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (15) of results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.29x