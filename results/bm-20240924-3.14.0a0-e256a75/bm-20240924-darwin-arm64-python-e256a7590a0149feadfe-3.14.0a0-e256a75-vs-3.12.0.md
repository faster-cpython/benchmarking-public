# Results vs. 3.12.0

- fork: python
- ref: e256a7590a0149feadfe
- machine: darwin-arm64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.60x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 160 ms: 1.06x faster                                                  |
| docutils       | 1.50 sec                                               | 1.42 sec: 1.06x faster                                                |
| tornado_http   | 69.3 ms                                                | 80.3 ms: 1.16x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 186 ms: 1.39x faster                                                  |
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 247 ms: 1.27x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 256 ms: 1.26x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 553 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 460 ms: 1.16x faster                                                  |
| async_tree_io              | 668 ms                                                 | 579 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 459 ms: 1.14x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.4 ms: 1.15x faster                                                 |
| nbody          | 68.8 ms                                                | 60.2 ms: 1.14x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 66.8 ms: 1.17x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.45 ms: 1.08x faster                                                 |
| regex_dna      | 154 ms                                                 | 144 ms: 1.07x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 183 us: 1.09x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 141 us: 1.07x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 52.3 ms: 1.07x faster                                                 |
| xml_etree_process    | 39.7 ms                                                | 37.4 ms: 1.06x faster                                                 |
| json_loads           | 17.2 us                                                | 16.8 us: 1.03x faster                                                 |
| unpickle_list        | 3.02 us                                                | 2.98 us: 1.01x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 73.5 ms: 1.01x faster                                                 |
| unpickle             | 9.12 us                                                | 9.05 us: 1.01x faster                                                 |
| json_dumps           | 6.22 ms                                                | 6.26 ms: 1.01x slower                                                 |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| xml_etree_parse      | 106 ms                                                 | 108 ms: 1.02x slower                                                  |
| pickle               | 7.23 us                                                | 7.39 us: 1.02x slower                                                 |
| pickle_list          | 2.89 us                                                | 2.98 us: 1.03x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 1.47 sec: 1.06x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 12.8 ms: 1.36x slower                                                 |
| python_startup         | 11.4 ms                                                | 15.7 ms: 1.38x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.37x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 20.0 ms: 1.12x faster                                                 |
| mako            | 7.71 ms                                                | 7.21 ms: 1.07x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.5 us: 1.67x faster                                                 |
| deepcopy                   | 235 us                                                 | 143 us: 1.64x faster                                                  |
| generators                 | 31.1 ms                                                | 20.7 ms: 1.50x faster                                                 |
| raytrace                   | 212 ms                                                 | 149 ms: 1.42x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 186 ms: 1.39x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.50 us: 1.38x faster                                                 |
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                                  |
| comprehensions             | 14.5 us                                                | 10.9 us: 1.34x faster                                                 |
| go                         | 102 ms                                                 | 79.2 ms: 1.28x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.12 ms: 1.28x faster                                                 |
| logging_silent             | 76.4 ns                                                | 60.3 ns: 1.27x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 247 ms: 1.27x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 256 ms: 1.26x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.01 us: 1.23x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 553 ms: 1.21x faster                                                  |
| logging_format             | 3.98 us                                                | 3.30 us: 1.21x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.0 ms: 1.20x faster                                                 |
| chaos                      | 42.5 ms                                                | 35.6 ms: 1.20x faster                                                 |
| unpack_sequence            | 31.5 ns                                                | 26.6 ns: 1.18x faster                                                 |
| nqueens                    | 62.4 ms                                                | 53.0 ms: 1.18x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 64.8 ms: 1.17x faster                                                 |
| regex_compile              | 77.9 ms                                                | 66.8 ms: 1.17x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.70 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 460 ms: 1.16x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 66.2 ms: 1.15x faster                                                 |
| async_tree_io              | 668 ms                                                 | 579 ms: 1.15x faster                                                  |
| float                      | 55.8 ms                                                | 48.4 ms: 1.15x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 740 us: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 459 ms: 1.14x faster                                                  |
| nbody                      | 68.8 ms                                                | 60.2 ms: 1.14x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 900 us: 1.13x faster                                                  |
| sympy_str                  | 148 ms                                                 | 131 ms: 1.12x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 69.2 ms: 1.12x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 166 ms: 1.12x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.06 ms: 1.12x faster                                                 |
| django_template            | 22.3 ms                                                | 20.0 ms: 1.12x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.42 sec: 1.11x faster                                                |
| bench_thread_pool          | 504 us                                                 | 454 us: 1.11x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 10.3 ms: 1.11x faster                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 30.9 ms: 1.10x faster                                                 |
| async_generators           | 304 ms                                                 | 278 ms: 1.09x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 183 us: 1.09x faster                                                  |
| scimark_fft                | 195 ms                                                 | 179 ms: 1.09x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 455 ms: 1.09x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 929 ms: 1.09x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 27.4 ms: 1.09x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.45 ms: 1.08x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 141 us: 1.07x faster                                                  |
| mako                       | 7.71 ms                                                | 7.21 ms: 1.07x faster                                                 |
| regex_dna                  | 154 ms                                                 | 144 ms: 1.07x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 52.3 ms: 1.07x faster                                                 |
| pycparser                  | 677 ms                                                 | 636 ms: 1.06x faster                                                  |
| sympy_expand               | 241 ms                                                 | 227 ms: 1.06x faster                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 42.4 ms: 1.06x faster                                                 |
| 2to3                       | 169 ms                                                 | 160 ms: 1.06x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 37.4 ms: 1.06x faster                                                 |
| json                       | 3.09 ms                                                | 2.92 ms: 1.06x faster                                                 |
| docutils                   | 1.50 sec                                               | 1.42 sec: 1.06x faster                                                |
| pathlib                    | 24.2 ms                                                | 23.3 ms: 1.04x faster                                                 |
| crypto_pyaes               | 51.9 ms                                                | 50.0 ms: 1.04x faster                                                 |
| json_loads                 | 17.2 us                                                | 16.8 us: 1.03x faster                                                 |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                                 |
| unpickle_list              | 3.02 us                                                | 2.98 us: 1.01x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 73.5 ms: 1.01x faster                                                 |
| unpickle                   | 9.12 us                                                | 9.05 us: 1.01x faster                                                 |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                  |
| richards_super             | 36.0 ms                                                | 36.2 ms: 1.01x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.26 ms: 1.01x slower                                                 |
| richards                   | 32.1 ms                                                | 32.4 ms: 1.01x slower                                                 |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| pyflate                    | 316 ms                                                 | 319 ms: 1.01x slower                                                  |
| xml_etree_parse            | 106 ms                                                 | 108 ms: 1.02x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.45 ms: 1.02x slower                                                 |
| pickle                     | 7.23 us                                                | 7.39 us: 1.02x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 16.4 ms: 1.02x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.28 sec: 1.03x slower                                                |
| pickle_list                | 2.89 us                                                | 2.98 us: 1.03x slower                                                 |
| fannkuch                   | 248 ms                                                 | 259 ms: 1.04x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.47 sec: 1.06x slower                                                |
| scimark_sor                | 87.4 ms                                                | 92.6 ms: 1.06x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 48.1 ms: 1.07x slower                                                 |
| coverage                   | 38.9 ms                                                | 44.1 ms: 1.14x slower                                                 |
| tornado_http               | 69.3 ms                                                | 80.3 ms: 1.16x slower                                                 |
| telco                      | 3.68 ms                                                | 4.63 ms: 1.26x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 889 us: 1.27x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 12.8 ms: 1.36x slower                                                 |
| python_startup             | 11.4 ms                                                | 15.7 ms: 1.38x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (4): asyncio_tcp, typing_runtime_protocols, meteor_contest, pidigits
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.60x