# Results vs. 3.12.0

- fork: python
- ref: c15f94d6fbc960790db3
- machine: darwin-arm64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.62x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 160 ms: 1.06x faster                                                   |
| chameleon      | 4.70 ms                                                | 4.33 ms: 1.08x faster                                                  |
| docutils       | 1.50 sec                                               | 1.44 sec: 1.05x faster                                                 |
| tornado_http   | 69.3 ms                                                | 65.8 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 236 ms: 1.37x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 194 ms: 1.33x faster                                                   |
| async_tree_none            | 266 ms                                                 | 207 ms: 1.28x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 255 ms: 1.22x faster                                                   |
| async_tree_io              | 668 ms                                                 | 552 ms: 1.21x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 553 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 448 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 464 ms: 1.13x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.3 ms: 1.15x faster                                                  |
| nbody          | 68.8 ms                                                | 59.7 ms: 1.15x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.3 ms: 1.14x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.58 ms: 1.02x faster                                                  |
| regex_dna      | 154 ms                                                 | 151 ms: 1.02x faster                                                   |
| regex_v8       | 16.0 ms                                                | 17.2 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 179 us: 1.12x faster                                                   |
| xml_etree_process    | 39.7 ms                                                | 36.9 ms: 1.08x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 141 us: 1.07x faster                                                   |
| xml_etree_generate   | 55.8 ms                                                | 52.5 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 71.1 ms: 1.04x faster                                                  |
| unpickle_list        | 3.02 us                                                | 2.91 us: 1.04x faster                                                  |
| json_loads           | 17.2 us                                                | 16.9 us: 1.02x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 104 ms: 1.02x faster                                                   |
| pickle_dict          | 18.1 us                                                | 18.3 us: 1.01x slower                                                  |
| pickle               | 7.23 us                                                | 7.46 us: 1.03x slower                                                  |
| pickle_list          | 2.89 us                                                | 2.99 us: 1.04x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.47 sec: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (2): json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 11.5 ms: 1.22x slower                                                  |
| python_startup         | 11.4 ms                                                | 14.4 ms: 1.26x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.24x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.4 ms: 1.15x faster                                                  |
| mako            | 7.71 ms                                                | 7.00 ms: 1.10x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| raytrace                   | 212 ms                                                 | 147 ms: 1.44x faster                                                   |
| comprehensions             | 14.5 us                                                | 10.2 us: 1.43x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 236 ms: 1.37x faster                                                   |
| generators                 | 31.1 ms                                                | 22.8 ms: 1.36x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 194 ms: 1.33x faster                                                   |
| async_tree_none            | 266 ms                                                 | 207 ms: 1.28x faster                                                   |
| logging_silent             | 76.4 ns                                                | 60.3 ns: 1.27x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.14 ms: 1.26x faster                                                  |
| chaos                      | 42.5 ms                                                | 34.1 ms: 1.25x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 255 ms: 1.22x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 22.7 us: 1.22x faster                                                  |
| coroutines                 | 19.2 ms                                                | 15.9 ms: 1.21x faster                                                  |
| async_tree_io              | 668 ms                                                 | 552 ms: 1.21x faster                                                   |
| logging_simple             | 3.69 us                                                | 3.05 us: 1.21x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 553 ms: 1.21x faster                                                   |
| logging_format             | 3.98 us                                                | 3.32 us: 1.20x faster                                                  |
| nqueens                    | 62.4 ms                                                | 52.5 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 448 ms: 1.19x faster                                                   |
| sqlglot_parse              | 848 us                                                 | 732 us: 1.16x faster                                                   |
| float                      | 55.8 ms                                                | 48.3 ms: 1.15x faster                                                  |
| nbody                      | 68.8 ms                                                | 59.7 ms: 1.15x faster                                                  |
| django_template            | 22.3 ms                                                | 19.4 ms: 1.15x faster                                                  |
| deepcopy                   | 235 us                                                 | 204 us: 1.15x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 66.5 ms: 1.15x faster                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 891 us: 1.15x faster                                                   |
| regex_compile              | 77.9 ms                                                | 68.3 ms: 1.14x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 66.7 ms: 1.14x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.82 us: 1.14x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 464 ms: 1.13x faster                                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.77 ms: 1.13x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.40 sec: 1.13x faster                                                 |
| sympy_sum                  | 77.6 ms                                                | 69.0 ms: 1.12x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 166 ms: 1.12x faster                                                   |
| pickle_pure_python         | 200 us                                                 | 179 us: 1.12x faster                                                   |
| sympy_str                  | 148 ms                                                 | 132 ms: 1.12x faster                                                   |
| hexiom                     | 4.54 ms                                                | 4.07 ms: 1.12x faster                                                  |
| mako                       | 7.71 ms                                                | 7.00 ms: 1.10x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 458 us: 1.10x faster                                                   |
| pathlib                    | 24.2 ms                                                | 22.0 ms: 1.10x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 31.0 ms: 1.10x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 10.4 ms: 1.10x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 27.5 ms: 1.08x faster                                                  |
| chameleon                  | 4.70 ms                                                | 4.33 ms: 1.08x faster                                                  |
| async_generators           | 304 ms                                                 | 281 ms: 1.08x faster                                                   |
| scimark_fft                | 195 ms                                                 | 181 ms: 1.08x faster                                                   |
| xml_etree_process          | 39.7 ms                                                | 36.9 ms: 1.08x faster                                                  |
| aiohttp                    | 1.08 ms                                                | 1.01 ms: 1.07x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 141 us: 1.07x faster                                                   |
| pycparser                  | 677 ms                                                 | 633 ms: 1.07x faster                                                   |
| sympy_expand               | 241 ms                                                 | 226 ms: 1.07x faster                                                   |
| gunicorn                   | 1.15 ms                                                | 1.07 ms: 1.07x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 466 ms: 1.07x faster                                                   |
| pprint_pformat             | 1.01 sec                                               | 949 ms: 1.07x faster                                                   |
| xml_etree_generate         | 55.8 ms                                                | 52.5 ms: 1.06x faster                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 42.5 ms: 1.06x faster                                                  |
| json                       | 3.09 ms                                                | 2.92 ms: 1.06x faster                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 88.0 us: 1.06x faster                                                  |
| 2to3                       | 169 ms                                                 | 160 ms: 1.06x faster                                                   |
| tornado_http               | 69.3 ms                                                | 65.8 ms: 1.05x faster                                                  |
| crypto_pyaes               | 51.9 ms                                                | 49.4 ms: 1.05x faster                                                  |
| docutils                   | 1.50 sec                                               | 1.44 sec: 1.05x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 71.1 ms: 1.04x faster                                                  |
| unpickle_list              | 3.02 us                                                | 2.91 us: 1.04x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.58 ms: 1.02x faster                                                  |
| regex_dna                  | 154 ms                                                 | 151 ms: 1.02x faster                                                   |
| json_loads                 | 17.2 us                                                | 16.9 us: 1.02x faster                                                  |
| richards_super             | 36.0 ms                                                | 35.3 ms: 1.02x faster                                                  |
| meteor_contest             | 71.7 ms                                                | 70.3 ms: 1.02x faster                                                  |
| xml_etree_parse            | 106 ms                                                 | 104 ms: 1.02x faster                                                   |
| dask                       | 222 ms                                                 | 218 ms: 1.02x faster                                                   |
| go                         | 102 ms                                                 | 100 ms: 1.01x faster                                                   |
| sqlite_synth               | 1.57 us                                                | 1.55 us: 1.01x faster                                                  |
| richards                   | 32.1 ms                                                | 31.7 ms: 1.01x faster                                                  |
| fannkuch                   | 248 ms                                                 | 248 ms: 1.00x faster                                                   |
| pyflate                    | 316 ms                                                 | 319 ms: 1.01x slower                                                   |
| pickle_dict                | 18.1 us                                                | 18.3 us: 1.01x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.02x slower                                                  |
| pickle                     | 7.23 us                                                | 7.46 us: 1.03x slower                                                  |
| pickle_list                | 2.89 us                                                | 2.99 us: 1.04x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 46.9 ms: 1.05x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.47 sec: 1.06x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.2 ms: 1.08x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 94.9 ms: 1.09x slower                                                  |
| coverage                   | 38.9 ms                                                | 45.0 ms: 1.16x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 11.5 ms: 1.22x slower                                                  |
| telco                      | 3.68 ms                                                | 4.61 ms: 1.25x slower                                                  |
| python_startup             | 11.4 ms                                                | 14.4 ms: 1.26x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 898 us: 1.28x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (7): asyncio_tcp, mypy2, asyncio_tcp_ssl, json_dumps, asyncio_websockets, pidigits, unpickle
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (14) of results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.62x