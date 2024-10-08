# Results vs. 3.12.0

- fork: mdboom
- ref: unicode_check_exact
- machine: darwin-arm64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 157 ms: 1.08x faster                                                 |
| docutils       | 1.50 sec                                               | 1.41 sec: 1.07x faster                                               |
| tornado_http   | 69.3 ms                                                | 84.2 ms: 1.21x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 187 ms: 1.38x faster                                                 |
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 246 ms: 1.27x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 258 ms: 1.25x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 541 ms: 1.24x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 462 ms: 1.15x faster                                                 |
| async_tree_io              | 668 ms                                                 | 582 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 461 ms: 1.14x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.0 ms: 1.14x faster                                                |
| nbody          | 68.8 ms                                                | 60.6 ms: 1.14x faster                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 67.5 ms: 1.15x faster                                                |
| regex_effbot   | 2.64 ms                                                | 2.45 ms: 1.08x faster                                                |
| regex_dna      | 154 ms                                                 | 145 ms: 1.07x faster                                                 |
| regex_v8       | 16.0 ms                                                | 16.5 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 182 us: 1.10x faster                                                 |
| unpickle_pure_python | 151 us                                                 | 140 us: 1.08x faster                                                 |
| xml_etree_process    | 39.7 ms                                                | 37.5 ms: 1.06x faster                                                |
| xml_etree_generate   | 55.8 ms                                                | 53.0 ms: 1.05x faster                                                |
| unpickle_list        | 3.02 us                                                | 2.90 us: 1.04x faster                                                |
| json_loads           | 17.2 us                                                | 17.1 us: 1.01x faster                                                |
| unpickle             | 9.12 us                                                | 9.24 us: 1.01x slower                                                |
| pickle_dict          | 18.1 us                                                | 18.4 us: 1.02x slower                                                |
| pickle               | 7.23 us                                                | 7.39 us: 1.02x slower                                                |
| json_dumps           | 6.22 ms                                                | 6.39 ms: 1.03x slower                                                |
| pickle_list          | 2.89 us                                                | 2.98 us: 1.03x slower                                                |
| xml_etree_parse      | 106 ms                                                 | 111 ms: 1.05x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 1.50 sec: 1.08x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.8 ms: 1.47x slower                                                |
| python_startup         | 11.4 ms                                                | 16.9 ms: 1.48x slower                                                |
| Geometric mean         | (ref)                                                  | 1.48x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.7 ms: 1.13x faster                                                |
| mako            | 7.71 ms                                                | 7.04 ms: 1.10x faster                                                |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.3 us: 1.69x faster                                                |
| deepcopy                   | 235 us                                                 | 144 us: 1.64x faster                                                 |
| generators                 | 31.1 ms                                                | 20.4 ms: 1.52x faster                                                |
| raytrace                   | 212 ms                                                 | 149 ms: 1.42x faster                                                 |
| deepcopy_reduce            | 2.07 us                                                | 1.50 us: 1.38x faster                                                |
| async_tree_none_tg         | 258 ms                                                 | 187 ms: 1.38x faster                                                 |
| comprehensions             | 14.5 us                                                | 10.6 us: 1.37x faster                                                |
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.11 ms: 1.28x faster                                                |
| go                         | 102 ms                                                 | 79.2 ms: 1.28x faster                                                |
| logging_silent             | 76.4 ns                                                | 60.0 ns: 1.27x faster                                                |
| async_tree_memoization     | 312 ms                                                 | 246 ms: 1.27x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 258 ms: 1.25x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 541 ms: 1.24x faster                                                 |
| logging_simple             | 3.69 us                                                | 3.05 us: 1.21x faster                                                |
| coroutines                 | 19.2 ms                                                | 16.0 ms: 1.20x faster                                                |
| logging_format             | 3.98 us                                                | 3.34 us: 1.19x faster                                                |
| chaos                      | 42.5 ms                                                | 35.8 ms: 1.19x faster                                                |
| unpack_sequence            | 31.5 ns                                                | 26.6 ns: 1.18x faster                                                |
| nqueens                    | 62.4 ms                                                | 53.3 ms: 1.17x faster                                                |
| regex_compile              | 77.9 ms                                                | 67.5 ms: 1.15x faster                                                |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 462 ms: 1.15x faster                                                 |
| async_tree_io              | 668 ms                                                 | 582 ms: 1.15x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 66.7 ms: 1.15x faster                                                |
| sqlglot_parse              | 848 us                                                 | 741 us: 1.14x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 461 ms: 1.14x faster                                                 |
| float                      | 55.8 ms                                                | 49.0 ms: 1.14x faster                                                |
| nbody                      | 68.8 ms                                                | 60.6 ms: 1.14x faster                                                |
| django_template            | 22.3 ms                                                | 19.7 ms: 1.13x faster                                                |
| sqlglot_transpile          | 1.02 ms                                                | 901 us: 1.13x faster                                                 |
| sympy_str                  | 148 ms                                                 | 131 ms: 1.13x faster                                                 |
| sympy_sum                  | 77.6 ms                                                | 68.8 ms: 1.13x faster                                                |
| bench_thread_pool          | 504 us                                                 | 448 us: 1.12x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.80 ms: 1.12x faster                                                |
| scimark_lu                 | 76.0 ms                                                | 68.0 ms: 1.12x faster                                                |
| sqlglot_normalize          | 186 ms                                                 | 167 ms: 1.11x faster                                                 |
| hexiom                     | 4.54 ms                                                | 4.10 ms: 1.11x faster                                                |
| mdp                        | 1.58 sec                                               | 1.43 sec: 1.11x faster                                               |
| sympy_integrate            | 11.4 ms                                                | 10.3 ms: 1.10x faster                                                |
| dulwich_log                | 29.8 ms                                                | 27.1 ms: 1.10x faster                                                |
| pickle_pure_python         | 200 us                                                 | 182 us: 1.10x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 454 ms: 1.10x faster                                                 |
| mako                       | 7.71 ms                                                | 7.04 ms: 1.10x faster                                                |
| pprint_pformat             | 1.01 sec                                               | 924 ms: 1.09x faster                                                 |
| async_generators           | 304 ms                                                 | 279 ms: 1.09x faster                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 31.3 ms: 1.09x faster                                                |
| regex_effbot               | 2.64 ms                                                | 2.45 ms: 1.08x faster                                                |
| 2to3                       | 169 ms                                                 | 157 ms: 1.08x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 140 us: 1.08x faster                                                 |
| docutils                   | 1.50 sec                                               | 1.41 sec: 1.07x faster                                               |
| regex_dna                  | 154 ms                                                 | 145 ms: 1.07x faster                                                 |
| pycparser                  | 677 ms                                                 | 636 ms: 1.06x faster                                                 |
| sympy_expand               | 241 ms                                                 | 227 ms: 1.06x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 37.5 ms: 1.06x faster                                                |
| scimark_fft                | 195 ms                                                 | 185 ms: 1.06x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 53.0 ms: 1.05x faster                                                |
| json                       | 3.09 ms                                                | 2.94 ms: 1.05x faster                                                |
| richards_super             | 36.0 ms                                                | 34.4 ms: 1.05x faster                                                |
| scimark_monte_carlo        | 45.0 ms                                                | 43.2 ms: 1.04x faster                                                |
| unpickle_list              | 3.02 us                                                | 2.90 us: 1.04x faster                                                |
| crypto_pyaes               | 51.9 ms                                                | 50.4 ms: 1.03x faster                                                |
| pathlib                    | 24.2 ms                                                | 23.6 ms: 1.03x faster                                                |
| richards                   | 32.1 ms                                                | 31.4 ms: 1.02x faster                                                |
| typing_runtime_protocols   | 93.0 us                                                | 91.0 us: 1.02x faster                                                |
| sqlite_synth               | 1.57 us                                                | 1.55 us: 1.01x faster                                                |
| json_loads                 | 17.2 us                                                | 17.1 us: 1.01x faster                                                |
| meteor_contest             | 71.7 ms                                                | 71.5 ms: 1.00x faster                                                |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                 |
| unpickle                   | 9.12 us                                                | 9.24 us: 1.01x slower                                                |
| pyflate                    | 316 ms                                                 | 321 ms: 1.02x slower                                                 |
| pickle_dict                | 18.1 us                                                | 18.4 us: 1.02x slower                                                |
| pickle                     | 7.23 us                                                | 7.39 us: 1.02x slower                                                |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.27 sec: 1.02x slower                                               |
| json_dumps                 | 6.22 ms                                                | 6.39 ms: 1.03x slower                                                |
| gc_traversal               | 2.40 ms                                                | 2.47 ms: 1.03x slower                                                |
| pickle_list                | 2.89 us                                                | 2.98 us: 1.03x slower                                                |
| regex_v8                   | 16.0 ms                                                | 16.5 ms: 1.03x slower                                                |
| xml_etree_parse            | 106 ms                                                 | 111 ms: 1.05x slower                                                 |
| fannkuch                   | 248 ms                                                 | 260 ms: 1.05x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 92.6 ms: 1.06x slower                                                |
| tomli_loads                | 1.39 sec                                               | 1.50 sec: 1.08x slower                                               |
| bench_mp_pool              | 44.9 ms                                                | 49.4 ms: 1.10x slower                                                |
| coverage                   | 38.9 ms                                                | 44.1 ms: 1.13x slower                                                |
| tornado_http               | 69.3 ms                                                | 84.2 ms: 1.21x slower                                                |
| create_gc_cycles           | 701 us                                                 | 898 us: 1.28x slower                                                 |
| telco                      | 3.68 ms                                                | 4.80 ms: 1.30x slower                                                |
| python_startup_no_site     | 9.37 ms                                                | 13.8 ms: 1.47x slower                                                |
| python_startup             | 11.4 ms                                                | 16.9 ms: 1.48x slower                                                |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                         |

Benchmark hidden because not significant (3): asyncio_tcp, xml_etree_iterparse, pidigits
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-darwin-arm64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.94x