# Results vs. 3.13.0b2

- fork: python
- ref: v3.12.0
- machine: darwin-arm64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 169 ms: 1.05x slower                                   |
| chameleon      | 4.27 ms                                                    | 4.70 ms: 1.10x slower                                  |
| docutils       | 1.44 sec                                                   | 1.50 sec: 1.04x slower                                 |
| tornado_http   | 66.7 ms                                                    | 69.3 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                      | 1.06x slower                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 467 ms                                                     | 526 ms: 1.12x slower                                   |
| async_tree_cpu_io_mixed_tg | 451 ms                                                     | 532 ms: 1.18x slower                                   |
| async_tree_io_tg           | 565 ms                                                     | 669 ms: 1.18x slower                                   |
| async_tree_io              | 563 ms                                                     | 668 ms: 1.19x slower                                   |
| async_tree_memoization     | 260 ms                                                     | 312 ms: 1.20x slower                                   |
| async_tree_none            | 209 ms                                                     | 266 ms: 1.27x slower                                   |
| async_tree_none_tg         | 198 ms                                                     | 258 ms: 1.30x slower                                   |
| async_tree_memoization_tg  | 240 ms                                                     | 323 ms: 1.35x slower                                   |
| Geometric mean             | (ref)                                                      | 1.22x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| float          | 48.6 ms                                                    | 55.8 ms: 1.15x slower                                  |
| nbody          | 59.6 ms                                                    | 68.8 ms: 1.16x slower                                  |
| Geometric mean | (ref)                                                      | 1.10x slower                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                  |
| regex_effbot   | 2.58 ms                                                    | 2.64 ms: 1.02x slower                                  |
| regex_dna      | 149 ms                                                     | 154 ms: 1.03x slower                                   |
| regex_compile  | 68.5 ms                                                    | 77.9 ms: 1.14x slower                                  |
| Geometric mean | (ref)                                                      | 1.03x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.39 sec: 1.05x faster                                 |
| pickle               | 7.48 us                                                    | 7.23 us: 1.03x faster                                  |
| pickle_list          | 2.96 us                                                    | 2.89 us: 1.02x faster                                  |
| pickle_dict          | 18.3 us                                                    | 18.1 us: 1.01x faster                                  |
| json_loads           | 16.8 us                                                    | 17.2 us: 1.02x slower                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 74.0 ms: 1.04x slower                                  |
| unpickle_list        | 2.88 us                                                    | 3.02 us: 1.05x slower                                  |
| xml_etree_generate   | 52.7 ms                                                    | 55.8 ms: 1.06x slower                                  |
| unpickle_pure_python | 141 us                                                     | 151 us: 1.07x slower                                   |
| xml_etree_process    | 37.1 ms                                                    | 39.7 ms: 1.07x slower                                  |
| pickle_pure_python   | 179 us                                                     | 200 us: 1.12x slower                                   |
| Geometric mean       | (ref)                                                      | 1.02x slower                                           |

Benchmark hidden because not significant (3): json_dumps, unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 11.4 ms: 1.33x faster                                  |
| python_startup_no_site | 12.3 ms                                                    | 9.37 ms: 1.31x faster                                  |
| Geometric mean         | (ref)                                                      | 1.32x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 7.71 ms: 1.10x slower                                  |
| django_template | 19.4 ms                                                    | 22.3 ms: 1.15x slower                                  |
| Geometric mean  | (ref)                                                      | 1.13x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| python_startup             | 15.2 ms                                                    | 11.4 ms: 1.33x faster                                  |
| python_startup_no_site     | 12.3 ms                                                    | 9.37 ms: 1.31x faster                                  |
| create_gc_cycles           | 897 us                                                     | 701 us: 1.28x faster                                   |
| telco                      | 4.60 ms                                                    | 3.68 ms: 1.25x faster                                  |
| coverage                   | 45.0 ms                                                    | 38.9 ms: 1.16x faster                                  |
| scimark_sor                | 94.9 ms                                                    | 87.4 ms: 1.09x faster                                  |
| regex_v8                   | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                  |
| tomli_loads                | 1.47 sec                                                   | 1.39 sec: 1.05x faster                                 |
| bench_mp_pool              | 47.2 ms                                                    | 44.9 ms: 1.05x faster                                  |
| asyncio_tcp_ssl            | 1.29 sec                                                   | 1.24 sec: 1.04x faster                                 |
| pickle                     | 7.48 us                                                    | 7.23 us: 1.03x faster                                  |
| pickle_list                | 2.96 us                                                    | 2.89 us: 1.02x faster                                  |
| gc_traversal               | 2.45 ms                                                    | 2.40 ms: 1.02x faster                                  |
| pyflate                    | 321 ms                                                     | 316 ms: 1.02x faster                                   |
| pickle_dict                | 18.3 us                                                    | 18.1 us: 1.01x faster                                  |
| richards                   | 31.8 ms                                                    | 32.1 ms: 1.01x slower                                  |
| go                         | 101 ms                                                     | 102 ms: 1.01x slower                                   |
| sqlite_synth               | 1.55 us                                                    | 1.57 us: 1.01x slower                                  |
| meteor_contest             | 70.3 ms                                                    | 71.7 ms: 1.02x slower                                  |
| regex_effbot               | 2.58 ms                                                    | 2.64 ms: 1.02x slower                                  |
| json_loads                 | 16.8 us                                                    | 17.2 us: 1.02x slower                                  |
| richards_super             | 35.2 ms                                                    | 36.0 ms: 1.02x slower                                  |
| mdp                        | 1.53 sec                                                   | 1.58 sec: 1.03x slower                                 |
| regex_dna                  | 149 ms                                                     | 154 ms: 1.03x slower                                   |
| xml_etree_iterparse        | 71.5 ms                                                    | 74.0 ms: 1.04x slower                                  |
| pathlib                    | 23.3 ms                                                    | 24.2 ms: 1.04x slower                                  |
| tornado_http               | 66.7 ms                                                    | 69.3 ms: 1.04x slower                                  |
| docutils                   | 1.44 sec                                                   | 1.50 sec: 1.04x slower                                 |
| unpickle_list              | 2.88 us                                                    | 3.02 us: 1.05x slower                                  |
| crypto_pyaes               | 49.5 ms                                                    | 51.9 ms: 1.05x slower                                  |
| 2to3                       | 161 ms                                                     | 169 ms: 1.05x slower                                   |
| json                       | 2.93 ms                                                    | 3.09 ms: 1.05x slower                                  |
| xml_etree_generate         | 52.7 ms                                                    | 55.8 ms: 1.06x slower                                  |
| scimark_monte_carlo        | 42.5 ms                                                    | 45.0 ms: 1.06x slower                                  |
| typing_runtime_protocols   | 87.6 us                                                    | 93.0 us: 1.06x slower                                  |
| pprint_pformat             | 947 ms                                                     | 1.01 sec: 1.07x slower                                 |
| sympy_expand               | 226 ms                                                     | 241 ms: 1.07x slower                                   |
| pprint_safe_repr           | 465 ms                                                     | 497 ms: 1.07x slower                                   |
| pycparser                  | 632 ms                                                     | 677 ms: 1.07x slower                                   |
| unpickle_pure_python       | 141 us                                                     | 151 us: 1.07x slower                                   |
| xml_etree_process          | 37.1 ms                                                    | 39.7 ms: 1.07x slower                                  |
| scimark_fft                | 181 ms                                                     | 195 ms: 1.08x slower                                   |
| async_generators           | 281 ms                                                     | 304 ms: 1.08x slower                                   |
| dulwich_log                | 27.6 ms                                                    | 29.8 ms: 1.08x slower                                  |
| aiohttp                    | 997 us                                                     | 1.08 ms: 1.08x slower                                  |
| sympy_integrate            | 10.3 ms                                                    | 11.4 ms: 1.10x slower                                  |
| chameleon                  | 4.27 ms                                                    | 4.70 ms: 1.10x slower                                  |
| sqlglot_optimize           | 30.9 ms                                                    | 34.0 ms: 1.10x slower                                  |
| mako                       | 6.99 ms                                                    | 7.71 ms: 1.10x slower                                  |
| gunicorn                   | 1.04 ms                                                    | 1.15 ms: 1.11x slower                                  |
| asyncio_tcp                | 402 ms                                                     | 449 ms: 1.12x slower                                   |
| hexiom                     | 4.06 ms                                                    | 4.54 ms: 1.12x slower                                  |
| pickle_pure_python         | 179 us                                                     | 200 us: 1.12x slower                                   |
| sqlglot_normalize          | 166 ms                                                     | 186 ms: 1.12x slower                                   |
| sympy_sum                  | 69.2 ms                                                    | 77.6 ms: 1.12x slower                                  |
| sympy_str                  | 131 ms                                                     | 148 ms: 1.12x slower                                   |
| async_tree_cpu_io_mixed    | 467 ms                                                     | 526 ms: 1.12x slower                                   |
| bench_thread_pool          | 447 us                                                     | 504 us: 1.13x slower                                   |
| scimark_sparse_mat_mult    | 2.77 ms                                                    | 3.14 ms: 1.13x slower                                  |
| scimark_lu                 | 66.9 ms                                                    | 76.0 ms: 1.14x slower                                  |
| regex_compile              | 68.5 ms                                                    | 77.9 ms: 1.14x slower                                  |
| deepcopy_reduce            | 1.82 us                                                    | 2.07 us: 1.14x slower                                  |
| sqlglot_transpile          | 891 us                                                     | 1.02 ms: 1.15x slower                                  |
| float                      | 48.6 ms                                                    | 55.8 ms: 1.15x slower                                  |
| django_template            | 19.4 ms                                                    | 22.3 ms: 1.15x slower                                  |
| deepcopy                   | 204 us                                                     | 235 us: 1.15x slower                                   |
| spectral_norm              | 66.4 ms                                                    | 76.4 ms: 1.15x slower                                  |
| nbody                      | 59.6 ms                                                    | 68.8 ms: 1.16x slower                                  |
| sqlglot_parse              | 732 us                                                     | 848 us: 1.16x slower                                   |
| async_tree_cpu_io_mixed_tg | 451 ms                                                     | 532 ms: 1.18x slower                                   |
| async_tree_io_tg           | 565 ms                                                     | 669 ms: 1.18x slower                                   |
| async_tree_io              | 563 ms                                                     | 668 ms: 1.19x slower                                   |
| nqueens                    | 52.2 ms                                                    | 62.4 ms: 1.20x slower                                  |
| async_tree_memoization     | 260 ms                                                     | 312 ms: 1.20x slower                                   |
| logging_format             | 3.31 us                                                    | 3.98 us: 1.20x slower                                  |
| logging_simple             | 3.04 us                                                    | 3.69 us: 1.21x slower                                  |
| coroutines                 | 15.8 ms                                                    | 19.2 ms: 1.21x slower                                  |
| deepcopy_memo              | 22.6 us                                                    | 27.7 us: 1.22x slower                                  |
| chaos                      | 34.0 ms                                                    | 42.5 ms: 1.25x slower                                  |
| deltablue                  | 2.14 ms                                                    | 2.71 ms: 1.26x slower                                  |
| async_tree_none            | 209 ms                                                     | 266 ms: 1.27x slower                                   |
| logging_silent             | 60.1 ns                                                    | 76.4 ns: 1.27x slower                                  |
| async_tree_none_tg         | 198 ms                                                     | 258 ms: 1.30x slower                                   |
| async_tree_memoization_tg  | 240 ms                                                     | 323 ms: 1.35x slower                                   |
| generators                 | 22.9 ms                                                    | 31.1 ms: 1.36x slower                                  |
| comprehensions             | 10.2 us                                                    | 14.5 us: 1.43x slower                                  |
| raytrace                   | 147 ms                                                     | 212 ms: 1.44x slower                                   |
| Geometric mean             | (ref)                                                      | 1.08x slower                                           |

Benchmark hidden because not significant (8): json_dumps, unpickle, pidigits, fannkuch, asyncio_websockets, mypy2, dask, xml_etree_parse
Ignored benchmarks (15) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 0.94x