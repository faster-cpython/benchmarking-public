# Results vs. 3.12.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: darwin-arm64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.041x faster
- HPT reliability: 98.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 181 ms: 1.07x slower                                                  |
| docutils       | 1.50 sec                                               | 1.57 sec: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 196 ms: 1.31x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 246 ms: 1.31x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 541 ms: 1.24x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 263 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 460 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 455 ms: 1.15x faster                                                  |
| async_tree_io              | 668 ms                                                 | 581 ms: 1.15x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.4 ms: 1.20x faster                                                 |
| nbody          | 68.8 ms                                                | 63.6 ms: 1.08x faster                                                 |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 148 ms: 1.05x faster                                                  |
| regex_compile  | 77.9 ms                                                | 76.1 ms: 1.02x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.61 ms: 1.01x faster                                                 |
| regex_v8       | 16.0 ms                                                | 16.8 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 39.7 ms                                                | 34.3 ms: 1.16x faster                                                 |
| unpickle_pure_python | 151 us                                                 | 131 us: 1.15x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 49.4 ms: 1.13x faster                                                 |
| pickle_pure_python   | 200 us                                                 | 177 us: 1.13x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.25 sec: 1.11x faster                                                |
| json_loads           | 17.2 us                                                | 16.5 us: 1.05x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 72.4 ms: 1.02x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 104 ms: 1.02x faster                                                  |
| json_dumps           | 6.22 ms                                                | 6.10 ms: 1.02x faster                                                 |
| unpickle_list        | 3.02 us                                                | 2.97 us: 1.02x faster                                                 |
| unpickle             | 9.12 us                                                | 9.03 us: 1.01x faster                                                 |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| pickle               | 7.23 us                                                | 7.36 us: 1.02x slower                                                 |
| pickle_list          | 2.89 us                                                | 3.01 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 14.8 ms: 1.58x slower                                                 |
| python_startup         | 11.4 ms                                                | 19.1 ms: 1.67x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.62x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.41 ms: 1.20x faster                                                 |
| django_template | 22.3 ms                                                | 23.0 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                  |
| deepcopy_memo              | 27.7 us                                                | 16.7 us: 1.66x faster                                                 |
| deepcopy                   | 235 us                                                 | 155 us: 1.52x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.51 us: 1.37x faster                                                 |
| logging_silent             | 76.4 ns                                                | 56.4 ns: 1.35x faster                                                 |
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 196 ms: 1.31x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 246 ms: 1.31x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 541 ms: 1.24x faster                                                  |
| generators                 | 31.1 ms                                                | 25.2 ms: 1.23x faster                                                 |
| mako                       | 7.71 ms                                                | 6.41 ms: 1.20x faster                                                 |
| float                      | 55.8 ms                                                | 46.4 ms: 1.20x faster                                                 |
| logging_simple             | 3.69 us                                                | 3.10 us: 1.19x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 263 ms: 1.19x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 64.1 ms: 1.19x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.3 ms: 1.18x faster                                                 |
| logging_format             | 3.98 us                                                | 3.41 us: 1.17x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 460 ms: 1.16x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 34.3 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 455 ms: 1.15x faster                                                  |
| async_tree_io              | 668 ms                                                 | 581 ms: 1.15x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 131 us: 1.15x faster                                                  |
| comprehensions             | 14.5 us                                                | 12.8 us: 1.14x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 49.4 ms: 1.13x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 177 us: 1.13x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.42 ms: 1.12x faster                                                 |
| raytrace                   | 212 ms                                                 | 191 ms: 1.11x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 68.7 ms: 1.11x faster                                                 |
| tomli_loads                | 1.39 sec                                               | 1.25 sec: 1.11x faster                                                |
| nqueens                    | 62.4 ms                                                | 57.1 ms: 1.09x faster                                                 |
| pathlib                    | 24.2 ms                                                | 22.3 ms: 1.08x faster                                                 |
| nbody                      | 68.8 ms                                                | 63.6 ms: 1.08x faster                                                 |
| json                       | 3.09 ms                                                | 2.89 ms: 1.07x faster                                                 |
| scimark_fft                | 195 ms                                                 | 185 ms: 1.06x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.50 sec: 1.05x faster                                                |
| bench_thread_pool          | 504 us                                                 | 480 us: 1.05x faster                                                  |
| async_generators           | 304 ms                                                 | 290 ms: 1.05x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.99 ms: 1.05x faster                                                 |
| regex_dna                  | 154 ms                                                 | 148 ms: 1.05x faster                                                  |
| json_loads                 | 17.2 us                                                | 16.5 us: 1.05x faster                                                 |
| chaos                      | 42.5 ms                                                | 41.0 ms: 1.04x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 29.0 ms: 1.03x faster                                                 |
| sqlite_synth               | 1.57 us                                                | 1.53 us: 1.02x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 72.4 ms: 1.02x faster                                                 |
| regex_compile              | 77.9 ms                                                | 76.1 ms: 1.02x faster                                                 |
| xml_etree_parse            | 106 ms                                                 | 104 ms: 1.02x faster                                                  |
| json_dumps                 | 6.22 ms                                                | 6.10 ms: 1.02x faster                                                 |
| unpickle_list              | 3.02 us                                                | 2.97 us: 1.02x faster                                                 |
| scimark_sor                | 87.4 ms                                                | 85.8 ms: 1.02x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.61 ms: 1.01x faster                                                 |
| unpickle                   | 9.12 us                                                | 9.03 us: 1.01x faster                                                 |
| pprint_pformat             | 1.01 sec                                               | 1.01 sec: 1.00x faster                                                |
| sqlglot_normalize          | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| pycparser                  | 677 ms                                                 | 682 ms: 1.01x slower                                                  |
| sqlglot_parse              | 848 us                                                 | 855 us: 1.01x slower                                                  |
| sympy_sum                  | 77.6 ms                                                | 78.3 ms: 1.01x slower                                                 |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| sympy_str                  | 148 ms                                                 | 150 ms: 1.01x slower                                                  |
| pprint_safe_repr           | 497 ms                                                 | 506 ms: 1.02x slower                                                  |
| pickle                     | 7.23 us                                                | 7.36 us: 1.02x slower                                                 |
| sympy_expand               | 241 ms                                                 | 246 ms: 1.02x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 95.0 us: 1.02x slower                                                 |
| pyflate                    | 316 ms                                                 | 323 ms: 1.02x slower                                                  |
| django_template            | 22.3 ms                                                | 23.0 ms: 1.03x slower                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.05 ms: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                                |
| pickle_list                | 2.89 us                                                | 3.01 us: 1.04x slower                                                 |
| docutils                   | 1.50 sec                                               | 1.57 sec: 1.04x slower                                                |
| regex_v8                   | 16.0 ms                                                | 16.8 ms: 1.05x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 76.3 ms: 1.06x slower                                                 |
| 2to3                       | 169 ms                                                 | 181 ms: 1.07x slower                                                  |
| fannkuch                   | 248 ms                                                 | 269 ms: 1.08x slower                                                  |
| richards_super             | 36.0 ms                                                | 39.0 ms: 1.08x slower                                                 |
| go                         | 102 ms                                                 | 110 ms: 1.09x slower                                                  |
| hexiom                     | 4.54 ms                                                | 4.96 ms: 1.09x slower                                                 |
| sympy_integrate            | 11.4 ms                                                | 12.5 ms: 1.10x slower                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 37.5 ms: 1.10x slower                                                 |
| richards                   | 32.1 ms                                                | 35.6 ms: 1.11x slower                                                 |
| coverage                   | 38.9 ms                                                | 43.9 ms: 1.13x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.91 ms: 1.21x slower                                                 |
| telco                      | 3.68 ms                                                | 4.50 ms: 1.22x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 62.2 ms: 1.39x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 14.8 ms: 1.58x slower                                                 |
| python_startup             | 11.4 ms                                                | 19.1 ms: 1.67x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 1.29 ms: 1.84x slower                                                 |
| unpack_sequence            | 31.5 ns                                                | 75.7 ns: 2.41x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (4): asyncio_tcp, scimark_monte_carlo, crypto_pyaes, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (15) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.041x faster
# HPT report

- Reliability score: 98.79% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.26x