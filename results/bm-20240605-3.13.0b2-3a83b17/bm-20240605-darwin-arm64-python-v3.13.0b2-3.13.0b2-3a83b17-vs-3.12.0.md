# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b2
- machine: darwin-arm64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 161 ms: 1.05x faster                                       |
| chameleon      | 4.70 ms                                                | 4.27 ms: 1.10x faster                                      |
| docutils       | 1.50 sec                                               | 1.44 sec: 1.04x faster                                     |
| tornado_http   | 69.3 ms                                                | 66.7 ms: 1.04x faster                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.35x faster                                       |
| async_tree_none_tg         | 258 ms                                                 | 198 ms: 1.30x faster                                       |
| async_tree_none            | 266 ms                                                 | 209 ms: 1.27x faster                                       |
| async_tree_memoization     | 312 ms                                                 | 260 ms: 1.20x faster                                       |
| async_tree_io              | 668 ms                                                 | 563 ms: 1.19x faster                                       |
| async_tree_io_tg           | 669 ms                                                 | 565 ms: 1.18x faster                                       |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 451 ms: 1.18x faster                                       |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 467 ms: 1.12x faster                                       |
| Geometric mean             | (ref)                                                  | 1.22x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 68.8 ms                                                | 59.6 ms: 1.16x faster                                      |
| float          | 55.8 ms                                                | 48.6 ms: 1.15x faster                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.5 ms: 1.14x faster                                      |
| regex_dna      | 154 ms                                                 | 149 ms: 1.03x faster                                       |
| regex_effbot   | 2.64 ms                                                | 2.58 ms: 1.02x faster                                      |
| regex_v8       | 16.0 ms                                                | 17.3 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 179 us: 1.12x faster                                       |
| xml_etree_process    | 39.7 ms                                                | 37.1 ms: 1.07x faster                                      |
| unpickle_pure_python | 151 us                                                 | 141 us: 1.07x faster                                       |
| xml_etree_generate   | 55.8 ms                                                | 52.7 ms: 1.06x faster                                      |
| unpickle_list        | 3.02 us                                                | 2.88 us: 1.05x faster                                      |
| xml_etree_iterparse  | 74.0 ms                                                | 71.5 ms: 1.04x faster                                      |
| json_loads           | 17.2 us                                                | 16.8 us: 1.02x faster                                      |
| pickle_dict          | 18.1 us                                                | 18.3 us: 1.01x slower                                      |
| pickle_list          | 2.89 us                                                | 2.96 us: 1.02x slower                                      |
| pickle               | 7.23 us                                                | 7.48 us: 1.03x slower                                      |
| tomli_loads          | 1.39 sec                                               | 1.47 sec: 1.05x slower                                     |
| Geometric mean       | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 12.3 ms: 1.31x slower                                      |
| python_startup         | 11.4 ms                                                | 15.2 ms: 1.33x slower                                      |
| Geometric mean         | (ref)                                                  | 1.32x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.4 ms: 1.15x faster                                      |
| mako            | 7.71 ms                                                | 6.99 ms: 1.10x faster                                      |
| Geometric mean  | (ref)                                                  | 1.13x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| raytrace                   | 212 ms                                                 | 147 ms: 1.44x faster                                       |
| comprehensions             | 14.5 us                                                | 10.2 us: 1.43x faster                                      |
| generators                 | 31.1 ms                                                | 22.9 ms: 1.36x faster                                      |
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.35x faster                                       |
| async_tree_none_tg         | 258 ms                                                 | 198 ms: 1.30x faster                                       |
| logging_silent             | 76.4 ns                                                | 60.1 ns: 1.27x faster                                      |
| async_tree_none            | 266 ms                                                 | 209 ms: 1.27x faster                                       |
| deltablue                  | 2.71 ms                                                | 2.14 ms: 1.26x faster                                      |
| chaos                      | 42.5 ms                                                | 34.0 ms: 1.25x faster                                      |
| deepcopy_memo              | 27.7 us                                                | 22.6 us: 1.22x faster                                      |
| coroutines                 | 19.2 ms                                                | 15.8 ms: 1.21x faster                                      |
| logging_simple             | 3.69 us                                                | 3.04 us: 1.21x faster                                      |
| logging_format             | 3.98 us                                                | 3.31 us: 1.20x faster                                      |
| async_tree_memoization     | 312 ms                                                 | 260 ms: 1.20x faster                                       |
| nqueens                    | 62.4 ms                                                | 52.2 ms: 1.20x faster                                      |
| async_tree_io              | 668 ms                                                 | 563 ms: 1.19x faster                                       |
| async_tree_io_tg           | 669 ms                                                 | 565 ms: 1.18x faster                                       |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 451 ms: 1.18x faster                                       |
| sqlglot_parse              | 848 us                                                 | 732 us: 1.16x faster                                       |
| nbody                      | 68.8 ms                                                | 59.6 ms: 1.16x faster                                      |
| spectral_norm              | 76.4 ms                                                | 66.4 ms: 1.15x faster                                      |
| deepcopy                   | 235 us                                                 | 204 us: 1.15x faster                                       |
| django_template            | 22.3 ms                                                | 19.4 ms: 1.15x faster                                      |
| float                      | 55.8 ms                                                | 48.6 ms: 1.15x faster                                      |
| sqlglot_transpile          | 1.02 ms                                                | 891 us: 1.15x faster                                       |
| deepcopy_reduce            | 2.07 us                                                | 1.82 us: 1.14x faster                                      |
| regex_compile              | 77.9 ms                                                | 68.5 ms: 1.14x faster                                      |
| scimark_lu                 | 76.0 ms                                                | 66.9 ms: 1.14x faster                                      |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.77 ms: 1.13x faster                                      |
| bench_thread_pool          | 504 us                                                 | 447 us: 1.13x faster                                       |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 467 ms: 1.12x faster                                       |
| sympy_str                  | 148 ms                                                 | 131 ms: 1.12x faster                                       |
| sympy_sum                  | 77.6 ms                                                | 69.2 ms: 1.12x faster                                      |
| sqlglot_normalize          | 186 ms                                                 | 166 ms: 1.12x faster                                       |
| pickle_pure_python         | 200 us                                                 | 179 us: 1.12x faster                                       |
| hexiom                     | 4.54 ms                                                | 4.06 ms: 1.12x faster                                      |
| asyncio_tcp                | 449 ms                                                 | 402 ms: 1.12x faster                                       |
| gunicorn                   | 1.15 ms                                                | 1.04 ms: 1.11x faster                                      |
| mako                       | 7.71 ms                                                | 6.99 ms: 1.10x faster                                      |
| sqlglot_optimize           | 34.0 ms                                                | 30.9 ms: 1.10x faster                                      |
| chameleon                  | 4.70 ms                                                | 4.27 ms: 1.10x faster                                      |
| sympy_integrate            | 11.4 ms                                                | 10.3 ms: 1.10x faster                                      |
| aiohttp                    | 1.08 ms                                                | 997 us: 1.08x faster                                       |
| dulwich_log                | 29.8 ms                                                | 27.6 ms: 1.08x faster                                      |
| async_generators           | 304 ms                                                 | 281 ms: 1.08x faster                                       |
| scimark_fft                | 195 ms                                                 | 181 ms: 1.08x faster                                       |
| xml_etree_process          | 39.7 ms                                                | 37.1 ms: 1.07x faster                                      |
| unpickle_pure_python       | 151 us                                                 | 141 us: 1.07x faster                                       |
| pycparser                  | 677 ms                                                 | 632 ms: 1.07x faster                                       |
| pprint_safe_repr           | 497 ms                                                 | 465 ms: 1.07x faster                                       |
| sympy_expand               | 241 ms                                                 | 226 ms: 1.07x faster                                       |
| pprint_pformat             | 1.01 sec                                               | 947 ms: 1.07x faster                                       |
| typing_runtime_protocols   | 93.0 us                                                | 87.6 us: 1.06x faster                                      |
| scimark_monte_carlo        | 45.0 ms                                                | 42.5 ms: 1.06x faster                                      |
| xml_etree_generate         | 55.8 ms                                                | 52.7 ms: 1.06x faster                                      |
| json                       | 3.09 ms                                                | 2.93 ms: 1.05x faster                                      |
| 2to3                       | 169 ms                                                 | 161 ms: 1.05x faster                                       |
| crypto_pyaes               | 51.9 ms                                                | 49.5 ms: 1.05x faster                                      |
| unpickle_list              | 3.02 us                                                | 2.88 us: 1.05x faster                                      |
| docutils                   | 1.50 sec                                               | 1.44 sec: 1.04x faster                                     |
| tornado_http               | 69.3 ms                                                | 66.7 ms: 1.04x faster                                      |
| pathlib                    | 24.2 ms                                                | 23.3 ms: 1.04x faster                                      |
| xml_etree_iterparse        | 74.0 ms                                                | 71.5 ms: 1.04x faster                                      |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.03x faster                                       |
| mdp                        | 1.58 sec                                               | 1.53 sec: 1.03x faster                                     |
| richards_super             | 36.0 ms                                                | 35.2 ms: 1.02x faster                                      |
| json_loads                 | 17.2 us                                                | 16.8 us: 1.02x faster                                      |
| regex_effbot               | 2.64 ms                                                | 2.58 ms: 1.02x faster                                      |
| meteor_contest             | 71.7 ms                                                | 70.3 ms: 1.02x faster                                      |
| sqlite_synth               | 1.57 us                                                | 1.55 us: 1.01x faster                                      |
| go                         | 102 ms                                                 | 101 ms: 1.01x faster                                       |
| richards                   | 32.1 ms                                                | 31.8 ms: 1.01x faster                                      |
| pickle_dict                | 18.1 us                                                | 18.3 us: 1.01x slower                                      |
| pyflate                    | 316 ms                                                 | 321 ms: 1.02x slower                                       |
| gc_traversal               | 2.40 ms                                                | 2.45 ms: 1.02x slower                                      |
| pickle_list                | 2.89 us                                                | 2.96 us: 1.02x slower                                      |
| pickle                     | 7.23 us                                                | 7.48 us: 1.03x slower                                      |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                     |
| bench_mp_pool              | 44.9 ms                                                | 47.2 ms: 1.05x slower                                      |
| tomli_loads                | 1.39 sec                                               | 1.47 sec: 1.05x slower                                     |
| regex_v8                   | 16.0 ms                                                | 17.3 ms: 1.08x slower                                      |
| scimark_sor                | 87.4 ms                                                | 94.9 ms: 1.09x slower                                      |
| coverage                   | 38.9 ms                                                | 45.0 ms: 1.16x slower                                      |
| telco                      | 3.68 ms                                                | 4.60 ms: 1.25x slower                                      |
| create_gc_cycles           | 701 us                                                 | 897 us: 1.28x slower                                       |
| python_startup_no_site     | 9.37 ms                                                | 12.3 ms: 1.31x slower                                      |
| python_startup             | 11.4 ms                                                | 15.2 ms: 1.33x slower                                      |
| Geometric mean             | (ref)                                                  | 1.08x faster                                               |

Benchmark hidden because not significant (8): xml_etree_parse, dask, mypy2, asyncio_websockets, fannkuch, pidigits, unpickle, json_dumps
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (15) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.07x