# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b4
- machine: darwin-arm64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.081x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 162 ms: 1.04x faster                                       |
| chameleon      | 4.70 ms                                                | 4.31 ms: 1.09x faster                                      |
| docutils       | 1.50 sec                                               | 1.45 sec: 1.04x faster                                     |
| tornado_http   | 69.3 ms                                                | 66.8 ms: 1.04x faster                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.34x faster                                       |
| async_tree_none_tg         | 258 ms                                                 | 199 ms: 1.30x faster                                       |
| async_tree_none            | 266 ms                                                 | 210 ms: 1.26x faster                                       |
| async_tree_memoization     | 312 ms                                                 | 260 ms: 1.20x faster                                       |
| async_tree_io              | 668 ms                                                 | 557 ms: 1.20x faster                                       |
| async_tree_io_tg           | 669 ms                                                 | 562 ms: 1.19x faster                                       |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 453 ms: 1.17x faster                                       |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 469 ms: 1.12x faster                                       |
| Geometric mean             | (ref)                                                  | 1.22x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 68.8 ms                                                | 59.8 ms: 1.15x faster                                      |
| float          | 55.8 ms                                                | 48.7 ms: 1.14x faster                                      |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.4 ms: 1.14x faster                                      |
| regex_dna      | 154 ms                                                 | 149 ms: 1.03x faster                                       |
| regex_effbot   | 2.64 ms                                                | 2.57 ms: 1.03x faster                                      |
| regex_v8       | 16.0 ms                                                | 17.2 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 180 us: 1.11x faster                                       |
| xml_etree_process    | 39.7 ms                                                | 37.3 ms: 1.06x faster                                      |
| unpickle_pure_python | 151 us                                                 | 142 us: 1.06x faster                                       |
| xml_etree_generate   | 55.8 ms                                                | 53.0 ms: 1.05x faster                                      |
| xml_etree_iterparse  | 74.0 ms                                                | 71.3 ms: 1.04x faster                                      |
| xml_etree_parse      | 106 ms                                                 | 105 ms: 1.02x faster                                       |
| json_loads           | 17.2 us                                                | 17.0 us: 1.01x faster                                      |
| json_dumps           | 6.22 ms                                                | 6.25 ms: 1.01x slower                                      |
| tomli_loads          | 1.39 sec                                               | 1.48 sec: 1.06x slower                                     |
| Geometric mean       | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 11.3 ms: 1.21x slower                                      |
| python_startup         | 11.4 ms                                                | 14.1 ms: 1.24x slower                                      |
| Geometric mean         | (ref)                                                  | 1.22x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.5 ms: 1.14x faster                                      |
| mako            | 7.71 ms                                                | 7.00 ms: 1.10x faster                                      |
| Geometric mean  | (ref)                                                  | 1.12x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| raytrace                   | 212 ms                                                 | 148 ms: 1.43x faster                                       |
| comprehensions             | 14.5 us                                                | 10.2 us: 1.43x faster                                      |
| generators                 | 31.1 ms                                                | 23.0 ms: 1.35x faster                                      |
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.34x faster                                       |
| async_tree_none_tg         | 258 ms                                                 | 199 ms: 1.30x faster                                       |
| logging_silent             | 76.4 ns                                                | 60.1 ns: 1.27x faster                                      |
| async_tree_none            | 266 ms                                                 | 210 ms: 1.26x faster                                       |
| deltablue                  | 2.71 ms                                                | 2.15 ms: 1.26x faster                                      |
| chaos                      | 42.5 ms                                                | 34.7 ms: 1.23x faster                                      |
| deepcopy_memo              | 27.7 us                                                | 22.7 us: 1.22x faster                                      |
| coroutines                 | 19.2 ms                                                | 15.9 ms: 1.21x faster                                      |
| async_tree_memoization     | 312 ms                                                 | 260 ms: 1.20x faster                                       |
| async_tree_io              | 668 ms                                                 | 557 ms: 1.20x faster                                       |
| async_tree_io_tg           | 669 ms                                                 | 562 ms: 1.19x faster                                       |
| logging_simple             | 3.69 us                                                | 3.11 us: 1.18x faster                                      |
| nqueens                    | 62.4 ms                                                | 52.9 ms: 1.18x faster                                      |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 453 ms: 1.17x faster                                       |
| logging_format             | 3.98 us                                                | 3.40 us: 1.17x faster                                      |
| sqlglot_parse              | 848 us                                                 | 730 us: 1.16x faster                                       |
| deepcopy                   | 235 us                                                 | 204 us: 1.15x faster                                       |
| nbody                      | 68.8 ms                                                | 59.8 ms: 1.15x faster                                      |
| sqlglot_transpile          | 1.02 ms                                                | 892 us: 1.15x faster                                       |
| float                      | 55.8 ms                                                | 48.7 ms: 1.14x faster                                      |
| django_template            | 22.3 ms                                                | 19.5 ms: 1.14x faster                                      |
| spectral_norm              | 76.4 ms                                                | 66.8 ms: 1.14x faster                                      |
| regex_compile              | 77.9 ms                                                | 68.4 ms: 1.14x faster                                      |
| scimark_lu                 | 76.0 ms                                                | 66.7 ms: 1.14x faster                                      |
| deepcopy_reduce            | 2.07 us                                                | 1.82 us: 1.14x faster                                      |
| mdp                        | 1.58 sec                                               | 1.41 sec: 1.12x faster                                     |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 469 ms: 1.12x faster                                       |
| sqlglot_normalize          | 186 ms                                                 | 166 ms: 1.12x faster                                       |
| sympy_str                  | 148 ms                                                 | 132 ms: 1.12x faster                                       |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.80 ms: 1.12x faster                                      |
| sympy_sum                  | 77.6 ms                                                | 69.5 ms: 1.12x faster                                      |
| hexiom                     | 4.54 ms                                                | 4.07 ms: 1.12x faster                                      |
| pickle_pure_python         | 200 us                                                 | 180 us: 1.11x faster                                       |
| sqlglot_optimize           | 34.0 ms                                                | 30.8 ms: 1.10x faster                                      |
| mako                       | 7.71 ms                                                | 7.00 ms: 1.10x faster                                      |
| sympy_integrate            | 11.4 ms                                                | 10.3 ms: 1.10x faster                                      |
| bench_thread_pool          | 504 us                                                 | 460 us: 1.10x faster                                       |
| chameleon                  | 4.70 ms                                                | 4.31 ms: 1.09x faster                                      |
| dulwich_log                | 29.8 ms                                                | 27.4 ms: 1.09x faster                                      |
| pprint_safe_repr           | 497 ms                                                 | 459 ms: 1.08x faster                                       |
| scimark_fft                | 195 ms                                                 | 181 ms: 1.08x faster                                       |
| pprint_pformat             | 1.01 sec                                               | 936 ms: 1.08x faster                                       |
| async_generators           | 304 ms                                                 | 282 ms: 1.08x faster                                       |
| pycparser                  | 677 ms                                                 | 630 ms: 1.07x faster                                       |
| sympy_expand               | 241 ms                                                 | 225 ms: 1.07x faster                                       |
| xml_etree_process          | 39.7 ms                                                | 37.3 ms: 1.06x faster                                      |
| unpickle_pure_python       | 151 us                                                 | 142 us: 1.06x faster                                       |
| scimark_monte_carlo        | 45.0 ms                                                | 42.6 ms: 1.06x faster                                      |
| json                       | 3.09 ms                                                | 2.92 ms: 1.06x faster                                      |
| xml_etree_generate         | 55.8 ms                                                | 53.0 ms: 1.05x faster                                      |
| richards_super             | 36.0 ms                                                | 34.3 ms: 1.05x faster                                      |
| typing_runtime_protocols   | 93.0 us                                                | 88.7 us: 1.05x faster                                      |
| 2to3                       | 169 ms                                                 | 162 ms: 1.04x faster                                       |
| tornado_http               | 69.3 ms                                                | 66.8 ms: 1.04x faster                                      |
| xml_etree_iterparse        | 74.0 ms                                                | 71.3 ms: 1.04x faster                                      |
| crypto_pyaes               | 51.9 ms                                                | 50.0 ms: 1.04x faster                                      |
| docutils                   | 1.50 sec                                               | 1.45 sec: 1.04x faster                                     |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.03x faster                                       |
| richards                   | 32.1 ms                                                | 31.2 ms: 1.03x faster                                      |
| regex_effbot               | 2.64 ms                                                | 2.57 ms: 1.03x faster                                      |
| pathlib                    | 24.2 ms                                                | 23.7 ms: 1.02x faster                                      |
| meteor_contest             | 71.7 ms                                                | 70.5 ms: 1.02x faster                                      |
| xml_etree_parse            | 106 ms                                                 | 105 ms: 1.02x faster                                       |
| json_loads                 | 17.2 us                                                | 17.0 us: 1.01x faster                                      |
| go                         | 102 ms                                                 | 100 ms: 1.01x faster                                       |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                       |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                       |
| json_dumps                 | 6.22 ms                                                | 6.25 ms: 1.01x slower                                      |
| pyflate                    | 316 ms                                                 | 321 ms: 1.02x slower                                       |
| gc_traversal               | 2.40 ms                                                | 2.45 ms: 1.02x slower                                      |
| fannkuch                   | 248 ms                                                 | 254 ms: 1.02x slower                                       |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.27 sec: 1.02x slower                                     |
| bench_mp_pool              | 44.9 ms                                                | 46.5 ms: 1.04x slower                                      |
| tomli_loads                | 1.39 sec                                               | 1.48 sec: 1.06x slower                                     |
| regex_v8                   | 16.0 ms                                                | 17.2 ms: 1.08x slower                                      |
| scimark_sor                | 87.4 ms                                                | 95.0 ms: 1.09x slower                                      |
| coverage                   | 38.9 ms                                                | 45.0 ms: 1.16x slower                                      |
| mypy2                      | 380 ms                                                 | 447 ms: 1.18x slower                                       |
| python_startup_no_site     | 9.37 ms                                                | 11.3 ms: 1.21x slower                                      |
| python_startup             | 11.4 ms                                                | 14.1 ms: 1.24x slower                                      |
| create_gc_cycles           | 701 us                                                 | 867 us: 1.24x slower                                       |
| telco                      | 3.68 ms                                                | 4.63 ms: 1.26x slower                                      |
| Geometric mean             | (ref)                                                  | 1.08x faster                                               |

Benchmark hidden because not significant (2): dask, asyncio_tcp
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240718-3.13.0b4-567c38b/bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.081x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.08x