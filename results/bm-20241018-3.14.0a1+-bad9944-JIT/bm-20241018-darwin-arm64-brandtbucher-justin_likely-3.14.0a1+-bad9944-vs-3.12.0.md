# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_likely
- machine: darwin-arm64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.034x faster
- HPT reliability: 98.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 183 ms: 1.08x slower                                                  |
| docutils       | 1.50 sec                                               | 1.58 sec: 1.05x slower                                                |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 234 ms: 1.38x faster                                                  |
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 244 ms: 1.28x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 213 ms: 1.21x faster                                                  |
| async_tree_io              | 668 ms                                                 | 581 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 470 ms: 1.13x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 611 ms: 1.10x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.2 ms: 1.16x faster                                                 |
| nbody          | 68.8 ms                                                | 65.3 ms: 1.05x faster                                                 |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                                  |
| regex_compile  | 77.9 ms                                                | 75.4 ms: 1.03x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.65 ms: 1.00x slower                                                 |
| regex_v8       | 16.0 ms                                                | 17.0 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                 | 132 us: 1.14x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 34.9 ms: 1.14x faster                                                 |
| pickle_pure_python   | 200 us                                                 | 179 us: 1.12x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.25 sec: 1.11x faster                                                |
| xml_etree_generate   | 55.8 ms                                                | 50.6 ms: 1.10x faster                                                 |
| json_loads           | 17.2 us                                                | 16.5 us: 1.04x faster                                                 |
| unpickle_list        | 3.02 us                                                | 2.97 us: 1.02x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 73.0 ms: 1.01x faster                                                 |
| unpickle             | 9.12 us                                                | 9.06 us: 1.01x faster                                                 |
| pickle_list          | 2.89 us                                                | 2.87 us: 1.00x faster                                                 |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| pickle               | 7.23 us                                                | 7.34 us: 1.02x slower                                                 |
| json_dumps           | 6.22 ms                                                | 7.13 ms: 1.15x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 14.7 ms: 1.57x slower                                                 |
| python_startup         | 11.4 ms                                                | 18.9 ms: 1.66x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.61x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.46 ms: 1.19x faster                                                 |
| django_template | 22.3 ms                                                | 22.7 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 241 ms: 1.70x faster                                                  |
| deepcopy_memo              | 27.7 us                                                | 17.0 us: 1.63x faster                                                 |
| deepcopy                   | 235 us                                                 | 155 us: 1.52x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 234 ms: 1.38x faster                                                  |
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.55 us: 1.34x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 244 ms: 1.28x faster                                                  |
| generators                 | 31.1 ms                                                | 25.4 ms: 1.23x faster                                                 |
| raytrace                   | 212 ms                                                 | 174 ms: 1.22x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 213 ms: 1.21x faster                                                  |
| mako                       | 7.71 ms                                                | 6.46 ms: 1.19x faster                                                 |
| logging_simple             | 3.69 us                                                | 3.12 us: 1.18x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 64.6 ms: 1.18x faster                                                 |
| logging_format             | 3.98 us                                                | 3.40 us: 1.17x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.5 ms: 1.16x faster                                                 |
| float                      | 55.8 ms                                                | 48.2 ms: 1.16x faster                                                 |
| async_tree_io              | 668 ms                                                 | 581 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 458 ms: 1.15x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 132 us: 1.14x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 34.9 ms: 1.14x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 470 ms: 1.13x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.41 ms: 1.12x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 179 us: 1.12x faster                                                  |
| tomli_loads                | 1.39 sec                                               | 1.25 sec: 1.11x faster                                                |
| comprehensions             | 14.5 us                                                | 13.1 us: 1.11x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 50.6 ms: 1.10x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 69.4 ms: 1.10x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 611 ms: 1.10x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.2 ms: 1.09x faster                                                 |
| logging_silent             | 76.4 ns                                                | 70.3 ns: 1.09x faster                                                 |
| json                       | 3.09 ms                                                | 2.84 ms: 1.09x faster                                                 |
| nqueens                    | 62.4 ms                                                | 58.6 ms: 1.07x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 473 us: 1.07x faster                                                  |
| nbody                      | 68.8 ms                                                | 65.3 ms: 1.05x faster                                                 |
| json_loads                 | 17.2 us                                                | 16.5 us: 1.04x faster                                                 |
| async_generators           | 304 ms                                                 | 292 ms: 1.04x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 28.7 ms: 1.04x faster                                                 |
| go                         | 102 ms                                                 | 97.9 ms: 1.04x faster                                                 |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                                  |
| regex_compile              | 77.9 ms                                                | 75.4 ms: 1.03x faster                                                 |
| chaos                      | 42.5 ms                                                | 41.3 ms: 1.03x faster                                                 |
| scimark_fft                | 195 ms                                                 | 190 ms: 1.03x faster                                                  |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                                 |
| unpickle_list              | 3.02 us                                                | 2.97 us: 1.02x faster                                                 |
| scimark_sor                | 87.4 ms                                                | 85.9 ms: 1.02x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 490 ms: 1.01x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 73.0 ms: 1.01x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.56 sec: 1.01x faster                                                |
| sqlglot_normalize          | 186 ms                                                 | 184 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 1.00 sec: 1.01x faster                                                |
| unpickle                   | 9.12 us                                                | 9.06 us: 1.01x faster                                                 |
| pickle_list                | 2.89 us                                                | 2.87 us: 1.00x faster                                                 |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| regex_effbot               | 2.64 ms                                                | 2.65 ms: 1.00x slower                                                 |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.16 ms: 1.01x slower                                                 |
| pycparser                  | 677 ms                                                 | 683 ms: 1.01x slower                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 45.6 ms: 1.01x slower                                                 |
| django_template            | 22.3 ms                                                | 22.7 ms: 1.02x slower                                                 |
| pickle                     | 7.23 us                                                | 7.34 us: 1.02x slower                                                 |
| sympy_sum                  | 77.6 ms                                                | 79.2 ms: 1.02x slower                                                 |
| sympy_expand               | 241 ms                                                 | 247 ms: 1.02x slower                                                  |
| sympy_str                  | 148 ms                                                 | 151 ms: 1.02x slower                                                  |
| sqlglot_parse              | 848 us                                                 | 871 us: 1.03x slower                                                  |
| pyflate                    | 316 ms                                                 | 326 ms: 1.03x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 53.7 ms: 1.04x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 74.4 ms: 1.04x slower                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.06 ms: 1.04x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.30 sec: 1.05x slower                                                |
| typing_runtime_protocols   | 93.0 us                                                | 97.8 us: 1.05x slower                                                 |
| docutils                   | 1.50 sec                                               | 1.58 sec: 1.05x slower                                                |
| regex_v8                   | 16.0 ms                                                | 17.0 ms: 1.07x slower                                                 |
| fannkuch                   | 248 ms                                                 | 266 ms: 1.07x slower                                                  |
| 2to3                       | 169 ms                                                 | 183 ms: 1.08x slower                                                  |
| hexiom                     | 4.54 ms                                                | 4.94 ms: 1.09x slower                                                 |
| richards_super             | 36.0 ms                                                | 39.3 ms: 1.09x slower                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 37.2 ms: 1.09x slower                                                 |
| sympy_integrate            | 11.4 ms                                                | 12.6 ms: 1.10x slower                                                 |
| richards                   | 32.1 ms                                                | 35.6 ms: 1.11x slower                                                 |
| coverage                   | 38.9 ms                                                | 43.8 ms: 1.13x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 7.13 ms: 1.15x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.95 ms: 1.23x slower                                                 |
| telco                      | 3.68 ms                                                | 4.57 ms: 1.24x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 62.0 ms: 1.38x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 14.7 ms: 1.57x slower                                                 |
| python_startup             | 11.4 ms                                                | 18.9 ms: 1.66x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 1.32 ms: 1.88x slower                                                 |
| unpack_sequence            | 31.5 ns                                                | 76.2 ns: 2.42x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (3): xml_etree_parse, asyncio_tcp, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (15) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-darwin-arm64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.034x faster
# HPT report

- Reliability score: 98.86% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.27x