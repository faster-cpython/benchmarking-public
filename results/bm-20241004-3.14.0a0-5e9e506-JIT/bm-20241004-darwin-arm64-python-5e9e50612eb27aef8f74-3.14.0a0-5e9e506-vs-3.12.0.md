# Results vs. 3.12.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: darwin-arm64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.04x faster
- HPT reliability: 99.13%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.63x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 180 ms: 1.06x slower                                                  |
| docutils       | 1.50 sec                                               | 1.58 sec: 1.05x slower                                                |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 186 ms: 1.38x faster                                                  |
| async_tree_none            | 266 ms                                                 | 200 ms: 1.33x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 250 ms: 1.25x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 260 ms: 1.24x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 571 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 457 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 461 ms: 1.14x faster                                                  |
| async_tree_io              | 668 ms                                                 | 587 ms: 1.14x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.3 ms: 1.21x faster                                                 |
| nbody          | 68.8 ms                                                | 63.5 ms: 1.08x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 147 ms: 1.05x faster                                                  |
| regex_compile  | 77.9 ms                                                | 75.7 ms: 1.03x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.68 ms: 1.02x slower                                                 |
| regex_v8       | 16.0 ms                                                | 16.9 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                 | 130 us: 1.16x faster                                                  |
| pickle_pure_python   | 200 us                                                 | 175 us: 1.14x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 34.7 ms: 1.14x faster                                                 |
| tomli_loads          | 1.39 sec                                               | 1.25 sec: 1.11x faster                                                |
| xml_etree_generate   | 55.8 ms                                                | 50.4 ms: 1.11x faster                                                 |
| json_loads           | 17.2 us                                                | 16.5 us: 1.05x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 71.7 ms: 1.03x faster                                                 |
| unpickle_list        | 3.02 us                                                | 2.97 us: 1.02x faster                                                 |
| json_dumps           | 6.22 ms                                                | 6.12 ms: 1.02x faster                                                 |
| unpickle             | 9.12 us                                                | 9.02 us: 1.01x faster                                                 |
| pickle_dict          | 18.1 us                                                | 18.1 us: 1.00x slower                                                 |
| pickle               | 7.23 us                                                | 7.41 us: 1.03x slower                                                 |
| pickle_list          | 2.89 us                                                | 2.99 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 16.2 ms: 1.42x slower                                                 |
| python_startup_no_site | 9.37 ms                                                | 13.3 ms: 1.42x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.42x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.35 ms: 1.21x faster                                                 |
| django_template | 22.3 ms                                                | 23.2 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.3 us: 1.70x faster                                                 |
| asyncio_websockets         | 409 ms                                                 | 241 ms: 1.70x faster                                                  |
| deepcopy                   | 235 us                                                 | 156 us: 1.51x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 186 ms: 1.38x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.52 us: 1.37x faster                                                 |
| async_tree_none            | 266 ms                                                 | 200 ms: 1.33x faster                                                  |
| logging_silent             | 76.4 ns                                                | 60.7 ns: 1.26x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 250 ms: 1.25x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 260 ms: 1.24x faster                                                  |
| generators                 | 31.1 ms                                                | 25.0 ms: 1.24x faster                                                 |
| mako                       | 7.71 ms                                                | 6.35 ms: 1.21x faster                                                 |
| float                      | 55.8 ms                                                | 46.3 ms: 1.21x faster                                                 |
| raytrace                   | 212 ms                                                 | 176 ms: 1.20x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.10 us: 1.19x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.2 ms: 1.19x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 64.1 ms: 1.19x faster                                                 |
| logging_format             | 3.98 us                                                | 3.38 us: 1.18x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 571 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 457 ms: 1.17x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 130 us: 1.16x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 175 us: 1.14x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 66.8 ms: 1.14x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 34.7 ms: 1.14x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 461 ms: 1.14x faster                                                  |
| async_tree_io              | 668 ms                                                 | 587 ms: 1.14x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.38 ms: 1.14x faster                                                 |
| comprehensions             | 14.5 us                                                | 12.9 us: 1.13x faster                                                 |
| tomli_loads                | 1.39 sec                                               | 1.25 sec: 1.11x faster                                                |
| xml_etree_generate         | 55.8 ms                                                | 50.4 ms: 1.11x faster                                                 |
| pathlib                    | 24.2 ms                                                | 22.0 ms: 1.10x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 462 us: 1.09x faster                                                  |
| nqueens                    | 62.4 ms                                                | 57.2 ms: 1.09x faster                                                 |
| nbody                      | 68.8 ms                                                | 63.5 ms: 1.08x faster                                                 |
| json                       | 3.09 ms                                                | 2.86 ms: 1.08x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.48 sec: 1.07x faster                                                |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.97 ms: 1.06x faster                                                 |
| scimark_fft                | 195 ms                                                 | 185 ms: 1.05x faster                                                  |
| async_generators           | 304 ms                                                 | 290 ms: 1.05x faster                                                  |
| regex_dna                  | 154 ms                                                 | 147 ms: 1.05x faster                                                  |
| json_loads                 | 17.2 us                                                | 16.5 us: 1.05x faster                                                 |
| chaos                      | 42.5 ms                                                | 40.7 ms: 1.05x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 71.7 ms: 1.03x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 29.0 ms: 1.03x faster                                                 |
| regex_compile              | 77.9 ms                                                | 75.7 ms: 1.03x faster                                                 |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                                 |
| unpickle_list              | 3.02 us                                                | 2.97 us: 1.02x faster                                                 |
| json_dumps                 | 6.22 ms                                                | 6.12 ms: 1.02x faster                                                 |
| pprint_pformat             | 1.01 sec                                               | 998 ms: 1.01x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 491 ms: 1.01x faster                                                  |
| unpickle                   | 9.12 us                                                | 9.02 us: 1.01x faster                                                 |
| go                         | 102 ms                                                 | 101 ms: 1.00x faster                                                  |
| pidigits                   | 282 ms                                                 | 282 ms: 1.00x slower                                                  |
| pickle_dict                | 18.1 us                                                | 18.1 us: 1.00x slower                                                 |
| sympy_sum                  | 77.6 ms                                                | 77.9 ms: 1.00x slower                                                 |
| sqlglot_normalize          | 186 ms                                                 | 187 ms: 1.01x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 52.4 ms: 1.01x slower                                                 |
| regex_effbot               | 2.64 ms                                                | 2.68 ms: 1.02x slower                                                 |
| sympy_str                  | 148 ms                                                 | 150 ms: 1.02x slower                                                  |
| pyflate                    | 316 ms                                                 | 322 ms: 1.02x slower                                                  |
| sympy_expand               | 241 ms                                                 | 247 ms: 1.02x slower                                                  |
| pickle                     | 7.23 us                                                | 7.41 us: 1.03x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.47 ms: 1.03x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 95.7 us: 1.03x slower                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.05 ms: 1.03x slower                                                 |
| hexiom                     | 4.54 ms                                                | 4.70 ms: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.03x slower                                                |
| pickle_list                | 2.89 us                                                | 2.99 us: 1.04x slower                                                 |
| django_template            | 22.3 ms                                                | 23.2 ms: 1.04x slower                                                 |
| fannkuch                   | 248 ms                                                 | 260 ms: 1.05x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.58 sec: 1.05x slower                                                |
| meteor_contest             | 71.7 ms                                                | 75.5 ms: 1.05x slower                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 47.7 ms: 1.06x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 16.9 ms: 1.06x slower                                                 |
| 2to3                       | 169 ms                                                 | 180 ms: 1.06x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 12.6 ms: 1.11x slower                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 37.7 ms: 1.11x slower                                                 |
| coverage                   | 38.9 ms                                                | 43.8 ms: 1.13x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 51.0 ms: 1.14x slower                                                 |
| telco                      | 3.68 ms                                                | 4.55 ms: 1.24x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 899 us: 1.28x slower                                                  |
| richards_super             | 36.0 ms                                                | 46.9 ms: 1.30x slower                                                 |
| richards                   | 32.1 ms                                                | 45.2 ms: 1.41x slower                                                 |
| python_startup             | 11.4 ms                                                | 16.2 ms: 1.42x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 13.3 ms: 1.42x slower                                                 |
| unpack_sequence            | 31.5 ns                                                | 75.8 ns: 2.41x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (6): scimark_sor, sqlglot_parse, pycparser, xml_etree_parse, asyncio_tcp, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.13% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.63x