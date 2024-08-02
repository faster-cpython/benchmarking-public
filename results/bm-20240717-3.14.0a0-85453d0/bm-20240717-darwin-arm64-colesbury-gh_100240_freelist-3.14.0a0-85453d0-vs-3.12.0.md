# Results vs. 3.12.0

- fork: colesbury
- ref: gh_100240_freelist
- machine: darwin-arm64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 163 ms: 1.04x faster                                                   |
| docutils       | 1.50 sec                                               | 1.45 sec: 1.03x faster                                                 |
| tornado_http   | 69.3 ms                                                | 66.6 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 174 ms: 1.48x faster                                                   |
| async_tree_none            | 266 ms                                                 | 192 ms: 1.38x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 230 ms: 1.36x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 239 ms: 1.35x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 507 ms: 1.32x faster                                                   |
| async_tree_io              | 668 ms                                                 | 522 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 444 ms: 1.20x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 450 ms: 1.17x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.6 ms: 1.15x faster                                                  |
| nbody          | 68.8 ms                                                | 61.7 ms: 1.12x faster                                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.6 ms: 1.13x faster                                                  |
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                                   |
| regex_effbot   | 2.64 ms                                                | 2.58 ms: 1.03x faster                                                  |
| regex_v8       | 16.0 ms                                                | 17.3 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 180 us: 1.11x faster                                                   |
| unpickle_pure_python | 151 us                                                 | 143 us: 1.05x faster                                                   |
| xml_etree_generate   | 55.8 ms                                                | 53.2 ms: 1.05x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 37.8 ms: 1.05x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 72.2 ms: 1.03x faster                                                  |
| json_loads           | 17.2 us                                                | 17.2 us: 1.00x faster                                                  |
| json_dumps           | 6.22 ms                                                | 6.52 ms: 1.05x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.48 sec: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 10.5 ms: 1.12x slower                                                  |
| python_startup         | 11.4 ms                                                | 13.4 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.15x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.8 ms: 1.13x faster                                                  |
| mako            | 7.71 ms                                                | 7.13 ms: 1.08x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.9 us: 1.64x faster                                                  |
| deepcopy                   | 235 us                                                 | 145 us: 1.62x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 174 ms: 1.48x faster                                                   |
| raytrace                   | 212 ms                                                 | 148 ms: 1.43x faster                                                   |
| deepcopy_reduce            | 2.07 us                                                | 1.49 us: 1.39x faster                                                  |
| async_tree_none            | 266 ms                                                 | 192 ms: 1.38x faster                                                   |
| generators                 | 31.1 ms                                                | 22.7 ms: 1.37x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 230 ms: 1.36x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 239 ms: 1.35x faster                                                   |
| comprehensions             | 14.5 us                                                | 10.9 us: 1.33x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 507 ms: 1.32x faster                                                   |
| deltablue                  | 2.71 ms                                                | 2.09 ms: 1.29x faster                                                  |
| logging_silent             | 76.4 ns                                                | 59.6 ns: 1.28x faster                                                  |
| async_tree_io              | 668 ms                                                 | 522 ms: 1.28x faster                                                   |
| logging_simple             | 3.69 us                                                | 3.03 us: 1.22x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 444 ms: 1.20x faster                                                   |
| logging_format             | 3.98 us                                                | 3.33 us: 1.19x faster                                                  |
| chaos                      | 42.5 ms                                                | 35.7 ms: 1.19x faster                                                  |
| coroutines                 | 19.2 ms                                                | 16.2 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 450 ms: 1.17x faster                                                   |
| nqueens                    | 62.4 ms                                                | 54.0 ms: 1.16x faster                                                  |
| float                      | 55.8 ms                                                | 48.6 ms: 1.15x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 741 us: 1.14x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 67.2 ms: 1.14x faster                                                  |
| regex_compile              | 77.9 ms                                                | 68.6 ms: 1.13x faster                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 902 us: 1.13x faster                                                   |
| django_template            | 22.3 ms                                                | 19.8 ms: 1.13x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 450 us: 1.12x faster                                                   |
| nbody                      | 68.8 ms                                                | 61.7 ms: 1.12x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 180 us: 1.11x faster                                                   |
| mdp                        | 1.58 sec                                               | 1.43 sec: 1.11x faster                                                 |
| sympy_sum                  | 77.6 ms                                                | 70.4 ms: 1.10x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.12 ms: 1.10x faster                                                  |
| sympy_str                  | 148 ms                                                 | 134 ms: 1.10x faster                                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.86 ms: 1.10x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 170 ms: 1.09x faster                                                   |
| sympy_integrate            | 11.4 ms                                                | 10.4 ms: 1.09x faster                                                  |
| mako                       | 7.71 ms                                                | 7.13 ms: 1.08x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 70.2 ms: 1.08x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 31.6 ms: 1.08x faster                                                  |
| async_generators           | 304 ms                                                 | 283 ms: 1.08x faster                                                   |
| pprint_pformat             | 1.01 sec                                               | 948 ms: 1.07x faster                                                   |
| pprint_safe_repr           | 497 ms                                                 | 468 ms: 1.06x faster                                                   |
| pycparser                  | 677 ms                                                 | 641 ms: 1.06x faster                                                   |
| unpickle_pure_python       | 151 us                                                 | 143 us: 1.05x faster                                                   |
| richards_super             | 36.0 ms                                                | 34.2 ms: 1.05x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 53.2 ms: 1.05x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 37.8 ms: 1.05x faster                                                  |
| scimark_fft                | 195 ms                                                 | 186 ms: 1.05x faster                                                   |
| pathlib                    | 24.2 ms                                                | 23.2 ms: 1.04x faster                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 43.2 ms: 1.04x faster                                                  |
| json                       | 3.09 ms                                                | 2.96 ms: 1.04x faster                                                  |
| sympy_expand               | 241 ms                                                 | 232 ms: 1.04x faster                                                   |
| 2to3                       | 169 ms                                                 | 163 ms: 1.04x faster                                                   |
| tornado_http               | 69.3 ms                                                | 66.6 ms: 1.04x faster                                                  |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                                   |
| docutils                   | 1.50 sec                                               | 1.45 sec: 1.03x faster                                                 |
| richards                   | 32.1 ms                                                | 31.2 ms: 1.03x faster                                                  |
| go                         | 102 ms                                                 | 98.9 ms: 1.03x faster                                                  |
| crypto_pyaes               | 51.9 ms                                                | 50.5 ms: 1.03x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.58 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 72.2 ms: 1.03x faster                                                  |
| json_loads                 | 17.2 us                                                | 17.2 us: 1.00x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                   |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| pyflate                    | 316 ms                                                 | 321 ms: 1.02x slower                                                   |
| gc_traversal               | 2.40 ms                                                | 2.45 ms: 1.02x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 95.0 us: 1.02x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 45.9 ms: 1.02x slower                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.27 sec: 1.02x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.52 ms: 1.05x slower                                                  |
| fannkuch                   | 248 ms                                                 | 263 ms: 1.06x slower                                                   |
| tomli_loads                | 1.39 sec                                               | 1.48 sec: 1.06x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.3 ms: 1.08x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 96.0 ms: 1.10x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 10.5 ms: 1.12x slower                                                  |
| coverage                   | 38.9 ms                                                | 45.3 ms: 1.17x slower                                                  |
| python_startup             | 11.4 ms                                                | 13.4 ms: 1.17x slower                                                  |
| telco                      | 3.68 ms                                                | 4.58 ms: 1.25x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 893 us: 1.27x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (3): asyncio_tcp, xml_etree_parse, meteor_contest
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240717-3.14.0a0-85453d0/bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.06x