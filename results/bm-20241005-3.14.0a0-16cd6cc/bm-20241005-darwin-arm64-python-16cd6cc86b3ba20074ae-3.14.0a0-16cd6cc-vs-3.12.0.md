# Results vs. 3.12.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: darwin-arm64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 0.79x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 161 ms: 1.05x faster                                                  |
| docutils       | 1.50 sec                                               | 1.40 sec: 1.08x faster                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 185 ms: 1.39x faster                                                  |
| async_tree_none            | 266 ms                                                 | 197 ms: 1.35x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 529 ms: 1.26x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 248 ms: 1.26x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 258 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 460 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                  |
| async_tree_io              | 668 ms                                                 | 585 ms: 1.14x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.8 ms: 1.14x faster                                                 |
| nbody          | 68.8 ms                                                | 65.7 ms: 1.05x faster                                                 |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 67.8 ms: 1.15x faster                                                 |
| regex_dna      | 154 ms                                                 | 148 ms: 1.05x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.62 ms: 1.01x faster                                                 |
| regex_v8       | 16.0 ms                                                | 16.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 182 us: 1.10x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 140 us: 1.08x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 52.3 ms: 1.07x faster                                                 |
| xml_etree_process    | 39.7 ms                                                | 37.4 ms: 1.06x faster                                                 |
| json_loads           | 17.2 us                                                | 16.5 us: 1.05x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 73.1 ms: 1.01x faster                                                 |
| unpickle_list        | 3.02 us                                                | 3.00 us: 1.01x faster                                                 |
| unpickle             | 9.12 us                                                | 9.07 us: 1.01x faster                                                 |
| json_dumps           | 6.22 ms                                                | 6.20 ms: 1.00x faster                                                 |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| xml_etree_parse      | 106 ms                                                 | 107 ms: 1.01x slower                                                  |
| pickle               | 7.23 us                                                | 7.33 us: 1.01x slower                                                 |
| pickle_list          | 2.89 us                                                | 3.00 us: 1.04x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 1.51 sec: 1.09x slower                                                |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.3 ms: 1.42x slower                                                 |
| python_startup         | 11.4 ms                                                | 16.3 ms: 1.43x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.43x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.7 ms: 1.14x faster                                                 |
| mako            | 7.71 ms                                                | 6.83 ms: 1.13x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 241 ms: 1.69x faster                                                  |
| deepcopy_memo              | 27.7 us                                                | 16.7 us: 1.65x faster                                                 |
| deepcopy                   | 235 us                                                 | 144 us: 1.64x faster                                                  |
| generators                 | 31.1 ms                                                | 20.6 ms: 1.51x faster                                                 |
| raytrace                   | 212 ms                                                 | 151 ms: 1.40x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 185 ms: 1.39x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.50 us: 1.38x faster                                                 |
| async_tree_none            | 266 ms                                                 | 197 ms: 1.35x faster                                                  |
| comprehensions             | 14.5 us                                                | 10.9 us: 1.33x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 529 ms: 1.26x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 248 ms: 1.26x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 258 ms: 1.25x faster                                                  |
| go                         | 102 ms                                                 | 81.6 ms: 1.25x faster                                                 |
| logging_silent             | 76.4 ns                                                | 61.5 ns: 1.24x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.22 ms: 1.22x faster                                                 |
| logging_simple             | 3.69 us                                                | 3.04 us: 1.21x faster                                                 |
| logging_format             | 3.98 us                                                | 3.32 us: 1.20x faster                                                 |
| nqueens                    | 62.4 ms                                                | 52.2 ms: 1.20x faster                                                 |
| chaos                      | 42.5 ms                                                | 36.0 ms: 1.18x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.4 ms: 1.18x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 65.2 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 460 ms: 1.16x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 736 us: 1.15x faster                                                  |
| regex_compile              | 77.9 ms                                                | 67.8 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                  |
| float                      | 55.8 ms                                                | 48.8 ms: 1.14x faster                                                 |
| async_tree_io              | 668 ms                                                 | 585 ms: 1.14x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.75 ms: 1.14x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 899 us: 1.14x faster                                                  |
| django_template            | 22.3 ms                                                | 19.7 ms: 1.14x faster                                                 |
| pathlib                    | 24.2 ms                                                | 21.4 ms: 1.13x faster                                                 |
| mako                       | 7.71 ms                                                | 6.83 ms: 1.13x faster                                                 |
| sympy_sum                  | 77.6 ms                                                | 68.8 ms: 1.13x faster                                                 |
| sympy_str                  | 148 ms                                                 | 132 ms: 1.12x faster                                                  |
| unpack_sequence            | 31.5 ns                                                | 28.1 ns: 1.12x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 166 ms: 1.12x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.08 ms: 1.11x faster                                                 |
| async_generators           | 304 ms                                                 | 274 ms: 1.11x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 30.8 ms: 1.11x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 455 us: 1.11x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 182 us: 1.10x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.44 sec: 1.10x faster                                                |
| json                       | 3.09 ms                                                | 2.82 ms: 1.10x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 27.4 ms: 1.09x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 70.3 ms: 1.09x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 458 ms: 1.08x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 936 ms: 1.08x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 140 us: 1.08x faster                                                  |
| docutils                   | 1.50 sec                                               | 1.40 sec: 1.08x faster                                                |
| sympy_expand               | 241 ms                                                 | 224 ms: 1.07x faster                                                  |
| pycparser                  | 677 ms                                                 | 632 ms: 1.07x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 52.3 ms: 1.07x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 37.4 ms: 1.06x faster                                                 |
| 2to3                       | 169 ms                                                 | 161 ms: 1.05x faster                                                  |
| nbody                      | 68.8 ms                                                | 65.7 ms: 1.05x faster                                                 |
| json_loads                 | 17.2 us                                                | 16.5 us: 1.05x faster                                                 |
| regex_dna                  | 154 ms                                                 | 148 ms: 1.05x faster                                                  |
| scimark_fft                | 195 ms                                                 | 187 ms: 1.04x faster                                                  |
| sqlite_synth               | 1.57 us                                                | 1.50 us: 1.04x faster                                                 |
| sympy_integrate            | 11.4 ms                                                | 10.9 ms: 1.04x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 43.7 ms: 1.03x faster                                                 |
| richards_super             | 36.0 ms                                                | 35.0 ms: 1.03x faster                                                 |
| richards                   | 32.1 ms                                                | 31.6 ms: 1.02x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 73.1 ms: 1.01x faster                                                 |
| crypto_pyaes               | 51.9 ms                                                | 51.3 ms: 1.01x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.62 ms: 1.01x faster                                                 |
| unpickle_list              | 3.02 us                                                | 3.00 us: 1.01x faster                                                 |
| unpickle                   | 9.12 us                                                | 9.07 us: 1.01x faster                                                 |
| json_dumps                 | 6.22 ms                                                | 6.20 ms: 1.00x faster                                                 |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| xml_etree_parse            | 106 ms                                                 | 107 ms: 1.01x slower                                                  |
| pickle                     | 7.23 us                                                | 7.33 us: 1.01x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 16.4 ms: 1.02x slower                                                 |
| pyflate                    | 316 ms                                                 | 325 ms: 1.03x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.47 ms: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                                |
| pickle_list                | 2.89 us                                                | 3.00 us: 1.04x slower                                                 |
| fannkuch                   | 248 ms                                                 | 263 ms: 1.06x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 48.6 ms: 1.08x slower                                                 |
| tomli_loads                | 1.39 sec                                               | 1.51 sec: 1.09x slower                                                |
| scimark_sor                | 87.4 ms                                                | 95.5 ms: 1.09x slower                                                 |
| coverage                   | 38.9 ms                                                | 43.7 ms: 1.13x slower                                                 |
| telco                      | 3.68 ms                                                | 4.56 ms: 1.24x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 900 us: 1.28x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 13.3 ms: 1.42x slower                                                 |
| python_startup             | 11.4 ms                                                | 16.3 ms: 1.43x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (4): typing_runtime_protocols, meteor_contest, asyncio_tcp, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 0.79x