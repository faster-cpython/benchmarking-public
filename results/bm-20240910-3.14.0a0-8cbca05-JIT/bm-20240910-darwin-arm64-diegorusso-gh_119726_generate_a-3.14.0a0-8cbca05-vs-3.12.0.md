# Results vs. 3.12.0

- fork: diegorusso
- ref: gh_119726_generate_a
- machine: darwin-arm64
- commit hash: 8cbca05
- commit date: 2024-09-10
- overall geometric mean: 1.03x faster
- HPT reliability: 96.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.54x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 176 ms: 1.04x slower                                                      |
| docutils       | 1.50 sec                                               | 1.56 sec: 1.04x slower                                                    |
| tornado_http   | 69.3 ms                                                | 83.7 ms: 1.21x slower                                                     |
| Geometric mean | (ref)                                                  | 1.09x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 188 ms: 1.37x faster                                                      |
| async_tree_none            | 266 ms                                                 | 200 ms: 1.33x faster                                                      |
| async_tree_memoization     | 312 ms                                                 | 248 ms: 1.26x faster                                                      |
| async_tree_io_tg           | 669 ms                                                 | 534 ms: 1.25x faster                                                      |
| async_tree_memoization_tg  | 323 ms                                                 | 259 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 464 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 462 ms: 1.14x faster                                                      |
| async_tree_io              | 668 ms                                                 | 592 ms: 1.13x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.6 ms: 1.20x faster                                                     |
| nbody          | 68.8 ms                                                | 63.3 ms: 1.09x faster                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.46 ms: 1.07x faster                                                     |
| regex_dna      | 154 ms                                                 | 145 ms: 1.06x faster                                                      |
| regex_compile  | 77.9 ms                                                | 73.9 ms: 1.05x faster                                                     |
| regex_v8       | 16.0 ms                                                | 16.5 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                 | 132 us: 1.14x faster                                                      |
| xml_etree_process    | 39.7 ms                                                | 34.8 ms: 1.14x faster                                                     |
| pickle_pure_python   | 200 us                                                 | 177 us: 1.13x faster                                                      |
| tomli_loads          | 1.39 sec                                               | 1.24 sec: 1.12x faster                                                    |
| xml_etree_generate   | 55.8 ms                                                | 51.2 ms: 1.09x faster                                                     |
| unpickle_list        | 3.02 us                                                | 2.90 us: 1.04x faster                                                     |
| xml_etree_iterparse  | 74.0 ms                                                | 72.3 ms: 1.02x faster                                                     |
| json_loads           | 17.2 us                                                | 17.1 us: 1.01x faster                                                     |
| pickle_dict          | 18.1 us                                                | 18.3 us: 1.01x slower                                                     |
| unpickle             | 9.12 us                                                | 9.25 us: 1.02x slower                                                     |
| pickle               | 7.23 us                                                | 7.37 us: 1.02x slower                                                     |
| pickle_list          | 2.89 us                                                | 2.94 us: 1.02x slower                                                     |
| json_dumps           | 6.22 ms                                                | 6.36 ms: 1.02x slower                                                     |
| xml_etree_parse      | 106 ms                                                 | 110 ms: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 14.2 ms: 1.51x slower                                                     |
| python_startup         | 11.4 ms                                                | 17.4 ms: 1.52x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.52x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.47 ms: 1.19x faster                                                     |
| django_template | 22.3 ms                                                | 22.6 ms: 1.01x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.2 us: 1.71x faster                                                     |
| deepcopy                   | 235 us                                                 | 155 us: 1.52x faster                                                      |
| async_tree_none_tg         | 258 ms                                                 | 188 ms: 1.37x faster                                                      |
| deepcopy_reduce            | 2.07 us                                                | 1.51 us: 1.37x faster                                                     |
| async_tree_none            | 266 ms                                                 | 200 ms: 1.33x faster                                                      |
| generators                 | 31.1 ms                                                | 24.4 ms: 1.27x faster                                                     |
| async_tree_memoization     | 312 ms                                                 | 248 ms: 1.26x faster                                                      |
| async_tree_io_tg           | 669 ms                                                 | 534 ms: 1.25x faster                                                      |
| async_tree_memoization_tg  | 323 ms                                                 | 259 ms: 1.25x faster                                                      |
| logging_simple             | 3.69 us                                                | 3.01 us: 1.23x faster                                                     |
| logging_silent             | 76.4 ns                                                | 62.5 ns: 1.22x faster                                                     |
| raytrace                   | 212 ms                                                 | 174 ms: 1.22x faster                                                      |
| logging_format             | 3.98 us                                                | 3.30 us: 1.21x faster                                                     |
| coroutines                 | 19.2 ms                                                | 16.0 ms: 1.20x faster                                                     |
| float                      | 55.8 ms                                                | 46.6 ms: 1.20x faster                                                     |
| mako                       | 7.71 ms                                                | 6.47 ms: 1.19x faster                                                     |
| scimark_lu                 | 76.0 ms                                                | 65.2 ms: 1.17x faster                                                     |
| deltablue                  | 2.71 ms                                                | 2.35 ms: 1.15x faster                                                     |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 464 ms: 1.15x faster                                                      |
| unpickle_pure_python       | 151 us                                                 | 132 us: 1.14x faster                                                      |
| xml_etree_process          | 39.7 ms                                                | 34.8 ms: 1.14x faster                                                     |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 462 ms: 1.14x faster                                                      |
| comprehensions             | 14.5 us                                                | 12.8 us: 1.13x faster                                                     |
| async_tree_io              | 668 ms                                                 | 592 ms: 1.13x faster                                                      |
| pickle_pure_python         | 200 us                                                 | 177 us: 1.13x faster                                                      |
| tomli_loads                | 1.39 sec                                               | 1.24 sec: 1.12x faster                                                    |
| spectral_norm              | 76.4 ms                                                | 68.1 ms: 1.12x faster                                                     |
| mdp                        | 1.58 sec                                               | 1.45 sec: 1.09x faster                                                    |
| xml_etree_generate         | 55.8 ms                                                | 51.2 ms: 1.09x faster                                                     |
| nbody                      | 68.8 ms                                                | 63.3 ms: 1.09x faster                                                     |
| regex_effbot               | 2.64 ms                                                | 2.46 ms: 1.07x faster                                                     |
| nqueens                    | 62.4 ms                                                | 58.3 ms: 1.07x faster                                                     |
| regex_dna                  | 154 ms                                                 | 145 ms: 1.06x faster                                                      |
| bench_thread_pool          | 504 us                                                 | 477 us: 1.06x faster                                                      |
| regex_compile              | 77.9 ms                                                | 73.9 ms: 1.05x faster                                                     |
| chaos                      | 42.5 ms                                                | 40.3 ms: 1.05x faster                                                     |
| json                       | 3.09 ms                                                | 2.95 ms: 1.05x faster                                                     |
| unpickle_list              | 3.02 us                                                | 2.90 us: 1.04x faster                                                     |
| dulwich_log                | 29.8 ms                                                | 28.8 ms: 1.04x faster                                                     |
| async_generators           | 304 ms                                                 | 294 ms: 1.03x faster                                                      |
| sympy_str                  | 148 ms                                                 | 144 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 74.0 ms                                                | 72.3 ms: 1.02x faster                                                     |
| sympy_sum                  | 77.6 ms                                                | 76.0 ms: 1.02x faster                                                     |
| scimark_fft                | 195 ms                                                 | 191 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.07 ms: 1.02x faster                                                     |
| sqlglot_normalize          | 186 ms                                                 | 183 ms: 1.02x faster                                                      |
| go                         | 102 ms                                                 | 101 ms: 1.01x faster                                                      |
| json_loads                 | 17.2 us                                                | 17.1 us: 1.01x faster                                                     |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                      |
| sqlite_synth               | 1.57 us                                                | 1.58 us: 1.00x slower                                                     |
| typing_runtime_protocols   | 93.0 us                                                | 94.0 us: 1.01x slower                                                     |
| sqlglot_parse              | 848 us                                                 | 858 us: 1.01x slower                                                      |
| django_template            | 22.3 ms                                                | 22.6 ms: 1.01x slower                                                     |
| pprint_safe_repr           | 497 ms                                                 | 503 ms: 1.01x slower                                                      |
| pickle_dict                | 18.1 us                                                | 18.3 us: 1.01x slower                                                     |
| unpickle                   | 9.12 us                                                | 9.25 us: 1.02x slower                                                     |
| scimark_sor                | 87.4 ms                                                | 88.9 ms: 1.02x slower                                                     |
| pprint_pformat             | 1.01 sec                                               | 1.03 sec: 1.02x slower                                                    |
| pickle                     | 7.23 us                                                | 7.37 us: 1.02x slower                                                     |
| pickle_list                | 2.89 us                                                | 2.94 us: 1.02x slower                                                     |
| sympy_integrate            | 11.4 ms                                                | 11.6 ms: 1.02x slower                                                     |
| sqlglot_transpile          | 1.02 ms                                                | 1.04 ms: 1.02x slower                                                     |
| json_dumps                 | 6.22 ms                                                | 6.36 ms: 1.02x slower                                                     |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.03x slower                                                     |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.28 sec: 1.03x slower                                                    |
| regex_v8                   | 16.0 ms                                                | 16.5 ms: 1.03x slower                                                     |
| xml_etree_parse            | 106 ms                                                 | 110 ms: 1.03x slower                                                      |
| sympy_expand               | 241 ms                                                 | 249 ms: 1.03x slower                                                      |
| hexiom                     | 4.54 ms                                                | 4.71 ms: 1.04x slower                                                     |
| 2to3                       | 169 ms                                                 | 176 ms: 1.04x slower                                                      |
| meteor_contest             | 71.7 ms                                                | 74.6 ms: 1.04x slower                                                     |
| sqlglot_optimize           | 34.0 ms                                                | 35.5 ms: 1.04x slower                                                     |
| docutils                   | 1.50 sec                                               | 1.56 sec: 1.04x slower                                                    |
| pyflate                    | 316 ms                                                 | 331 ms: 1.05x slower                                                      |
| fannkuch                   | 248 ms                                                 | 267 ms: 1.08x slower                                                      |
| scimark_monte_carlo        | 45.0 ms                                                | 48.6 ms: 1.08x slower                                                     |
| bench_mp_pool              | 44.9 ms                                                | 52.2 ms: 1.16x slower                                                     |
| coverage                   | 38.9 ms                                                | 45.4 ms: 1.17x slower                                                     |
| tornado_http               | 69.3 ms                                                | 83.7 ms: 1.21x slower                                                     |
| create_gc_cycles           | 701 us                                                 | 903 us: 1.29x slower                                                      |
| telco                      | 3.68 ms                                                | 4.76 ms: 1.29x slower                                                     |
| richards_super             | 36.0 ms                                                | 46.8 ms: 1.30x slower                                                     |
| richards                   | 32.1 ms                                                | 45.0 ms: 1.40x slower                                                     |
| python_startup_no_site     | 9.37 ms                                                | 14.2 ms: 1.51x slower                                                     |
| python_startup             | 11.4 ms                                                | 17.4 ms: 1.52x slower                                                     |
| unpack_sequence            | 31.5 ns                                                | 76.1 ns: 2.42x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (5): asyncio_tcp, crypto_pyaes, pidigits, pycparser, pathlib
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20240910-3.14.0a0-8cbca05-JIT/bm-20240910-darwin-arm64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.71% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.54x