# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: darwin-arm64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.088x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 162 ms: 1.04x faster                                         |
| docutils       | 1.50 sec                                               | 1.43 sec: 1.05x faster                                       |
| tornado_http   | 69.3 ms                                                | 82.2 ms: 1.19x slower                                        |
| Geometric mean | (ref)                                                  | 1.03x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 189 ms: 1.37x faster                                         |
| async_tree_none            | 266 ms                                                 | 200 ms: 1.33x faster                                         |
| async_tree_memoization     | 312 ms                                                 | 247 ms: 1.27x faster                                         |
| async_tree_memoization_tg  | 323 ms                                                 | 258 ms: 1.25x faster                                         |
| async_tree_io_tg           | 669 ms                                                 | 556 ms: 1.20x faster                                         |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 462 ms: 1.15x faster                                         |
| async_tree_io              | 668 ms                                                 | 583 ms: 1.15x faster                                         |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 460 ms: 1.14x faster                                         |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 68.8 ms                                                | 59.6 ms: 1.16x faster                                        |
| float          | 55.8 ms                                                | 48.9 ms: 1.14x faster                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 67.4 ms: 1.15x faster                                        |
| regex_effbot   | 2.64 ms                                                | 2.46 ms: 1.07x faster                                        |
| regex_dna      | 154 ms                                                 | 145 ms: 1.07x faster                                         |
| regex_v8       | 16.0 ms                                                | 16.4 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 184 us: 1.09x faster                                         |
| unpickle_pure_python | 151 us                                                 | 140 us: 1.08x faster                                         |
| xml_etree_process    | 39.7 ms                                                | 37.6 ms: 1.06x faster                                        |
| xml_etree_generate   | 55.8 ms                                                | 53.5 ms: 1.04x faster                                        |
| unpickle_list        | 3.02 us                                                | 2.92 us: 1.03x faster                                        |
| json_loads           | 17.2 us                                                | 17.1 us: 1.01x faster                                        |
| pickle_dict          | 18.1 us                                                | 18.3 us: 1.01x slower                                        |
| pickle               | 7.23 us                                                | 7.40 us: 1.02x slower                                        |
| xml_etree_parse      | 106 ms                                                 | 109 ms: 1.02x slower                                         |
| unpickle             | 9.12 us                                                | 9.43 us: 1.03x slower                                        |
| pickle_list          | 2.89 us                                                | 2.99 us: 1.03x slower                                        |
| json_dumps           | 6.22 ms                                                | 6.46 ms: 1.04x slower                                        |
| tomli_loads          | 1.39 sec                                               | 1.48 sec: 1.06x slower                                       |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 16.5 ms: 1.45x slower                                        |
| python_startup_no_site | 9.37 ms                                                | 13.6 ms: 1.45x slower                                        |
| Geometric mean         | (ref)                                                  | 1.45x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.8 ms: 1.13x faster                                        |
| mako            | 7.71 ms                                                | 6.97 ms: 1.11x faster                                        |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.4 us: 1.68x faster                                        |
| deepcopy                   | 235 us                                                 | 144 us: 1.63x faster                                         |
| generators                 | 31.1 ms                                                | 20.8 ms: 1.50x faster                                        |
| comprehensions             | 14.5 us                                                | 10.1 us: 1.44x faster                                        |
| raytrace                   | 212 ms                                                 | 149 ms: 1.42x faster                                         |
| deepcopy_reduce            | 2.07 us                                                | 1.50 us: 1.38x faster                                        |
| async_tree_none_tg         | 258 ms                                                 | 189 ms: 1.37x faster                                         |
| async_tree_none            | 266 ms                                                 | 200 ms: 1.33x faster                                         |
| go                         | 102 ms                                                 | 79.3 ms: 1.28x faster                                        |
| async_tree_memoization     | 312 ms                                                 | 247 ms: 1.27x faster                                         |
| deltablue                  | 2.71 ms                                                | 2.14 ms: 1.27x faster                                        |
| logging_silent             | 76.4 ns                                                | 60.6 ns: 1.26x faster                                        |
| async_tree_memoization_tg  | 323 ms                                                 | 258 ms: 1.25x faster                                         |
| logging_simple             | 3.69 us                                                | 3.03 us: 1.22x faster                                        |
| async_tree_io_tg           | 669 ms                                                 | 556 ms: 1.20x faster                                         |
| logging_format             | 3.98 us                                                | 3.32 us: 1.20x faster                                        |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.19x faster                                        |
| chaos                      | 42.5 ms                                                | 35.7 ms: 1.19x faster                                        |
| unpack_sequence            | 31.5 ns                                                | 26.5 ns: 1.19x faster                                        |
| nqueens                    | 62.4 ms                                                | 53.6 ms: 1.16x faster                                        |
| nbody                      | 68.8 ms                                                | 59.6 ms: 1.16x faster                                        |
| regex_compile              | 77.9 ms                                                | 67.4 ms: 1.15x faster                                        |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 462 ms: 1.15x faster                                         |
| async_tree_io              | 668 ms                                                 | 583 ms: 1.15x faster                                         |
| sqlglot_parse              | 848 us                                                 | 741 us: 1.14x faster                                         |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 460 ms: 1.14x faster                                         |
| float                      | 55.8 ms                                                | 48.9 ms: 1.14x faster                                        |
| scimark_lu                 | 76.0 ms                                                | 67.0 ms: 1.13x faster                                        |
| spectral_norm              | 76.4 ms                                                | 67.5 ms: 1.13x faster                                        |
| django_template            | 22.3 ms                                                | 19.8 ms: 1.13x faster                                        |
| sqlglot_transpile          | 1.02 ms                                                | 908 us: 1.13x faster                                         |
| sympy_sum                  | 77.6 ms                                                | 69.0 ms: 1.12x faster                                        |
| hexiom                     | 4.54 ms                                                | 4.05 ms: 1.12x faster                                        |
| bench_thread_pool          | 504 us                                                 | 450 us: 1.12x faster                                         |
| sympy_str                  | 148 ms                                                 | 132 ms: 1.12x faster                                         |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.81 ms: 1.11x faster                                        |
| sqlglot_normalize          | 186 ms                                                 | 167 ms: 1.11x faster                                         |
| mako                       | 7.71 ms                                                | 6.97 ms: 1.11x faster                                        |
| mdp                        | 1.58 sec                                               | 1.43 sec: 1.10x faster                                       |
| sympy_integrate            | 11.4 ms                                                | 10.3 ms: 1.10x faster                                        |
| dulwich_log                | 29.8 ms                                                | 27.3 ms: 1.09x faster                                        |
| pprint_safe_repr           | 497 ms                                                 | 456 ms: 1.09x faster                                         |
| sqlglot_optimize           | 34.0 ms                                                | 31.3 ms: 1.09x faster                                        |
| pickle_pure_python         | 200 us                                                 | 184 us: 1.09x faster                                         |
| pprint_pformat             | 1.01 sec                                               | 932 ms: 1.08x faster                                         |
| async_generators           | 304 ms                                                 | 282 ms: 1.08x faster                                         |
| unpickle_pure_python       | 151 us                                                 | 140 us: 1.08x faster                                         |
| regex_effbot               | 2.64 ms                                                | 2.46 ms: 1.07x faster                                        |
| regex_dna                  | 154 ms                                                 | 145 ms: 1.07x faster                                         |
| pycparser                  | 677 ms                                                 | 638 ms: 1.06x faster                                         |
| scimark_fft                | 195 ms                                                 | 184 ms: 1.06x faster                                         |
| sympy_expand               | 241 ms                                                 | 228 ms: 1.06x faster                                         |
| xml_etree_process          | 39.7 ms                                                | 37.6 ms: 1.06x faster                                        |
| docutils                   | 1.50 sec                                               | 1.43 sec: 1.05x faster                                       |
| scimark_monte_carlo        | 45.0 ms                                                | 43.1 ms: 1.05x faster                                        |
| 2to3                       | 169 ms                                                 | 162 ms: 1.04x faster                                         |
| xml_etree_generate         | 55.8 ms                                                | 53.5 ms: 1.04x faster                                        |
| json                       | 3.09 ms                                                | 2.97 ms: 1.04x faster                                        |
| unpickle_list              | 3.02 us                                                | 2.92 us: 1.03x faster                                        |
| crypto_pyaes               | 51.9 ms                                                | 50.3 ms: 1.03x faster                                        |
| typing_runtime_protocols   | 93.0 us                                                | 90.4 us: 1.03x faster                                        |
| pathlib                    | 24.2 ms                                                | 23.6 ms: 1.03x faster                                        |
| sqlite_synth               | 1.57 us                                                | 1.56 us: 1.01x faster                                        |
| json_loads                 | 17.2 us                                                | 17.1 us: 1.01x faster                                        |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                         |
| meteor_contest             | 71.7 ms                                                | 71.6 ms: 1.00x faster                                        |
| richards                   | 32.1 ms                                                | 32.3 ms: 1.01x slower                                        |
| pickle_dict                | 18.1 us                                                | 18.3 us: 1.01x slower                                        |
| pyflate                    | 316 ms                                                 | 322 ms: 1.02x slower                                         |
| gc_traversal               | 2.40 ms                                                | 2.45 ms: 1.02x slower                                        |
| pickle                     | 7.23 us                                                | 7.40 us: 1.02x slower                                        |
| xml_etree_parse            | 106 ms                                                 | 109 ms: 1.02x slower                                         |
| regex_v8                   | 16.0 ms                                                | 16.4 ms: 1.03x slower                                        |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.28 sec: 1.03x slower                                       |
| unpickle                   | 9.12 us                                                | 9.43 us: 1.03x slower                                        |
| pickle_list                | 2.89 us                                                | 2.99 us: 1.03x slower                                        |
| json_dumps                 | 6.22 ms                                                | 6.46 ms: 1.04x slower                                        |
| fannkuch                   | 248 ms                                                 | 260 ms: 1.05x slower                                         |
| tomli_loads                | 1.39 sec                                               | 1.48 sec: 1.06x slower                                       |
| scimark_sor                | 87.4 ms                                                | 93.5 ms: 1.07x slower                                        |
| bench_mp_pool              | 44.9 ms                                                | 48.5 ms: 1.08x slower                                        |
| coverage                   | 38.9 ms                                                | 44.9 ms: 1.16x slower                                        |
| tornado_http               | 69.3 ms                                                | 82.2 ms: 1.19x slower                                        |
| create_gc_cycles           | 701 us                                                 | 888 us: 1.27x slower                                         |
| telco                      | 3.68 ms                                                | 4.87 ms: 1.32x slower                                        |
| python_startup             | 11.4 ms                                                | 16.5 ms: 1.45x slower                                        |
| python_startup_no_site     | 9.37 ms                                                | 13.6 ms: 1.45x slower                                        |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                 |

Benchmark hidden because not significant (4): asyncio_tcp, xml_etree_iterparse, richards_super, pidigits
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.088x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.51x