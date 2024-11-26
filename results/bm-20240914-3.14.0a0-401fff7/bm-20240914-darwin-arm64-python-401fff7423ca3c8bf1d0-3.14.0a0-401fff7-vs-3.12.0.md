# Results vs. 3.12.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: darwin-arm64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.090x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.48x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 159 ms: 1.06x faster                                                  |
| docutils       | 1.50 sec                                               | 1.40 sec: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 189 ms: 1.36x faster                                                  |
| async_tree_none            | 266 ms                                                 | 199 ms: 1.34x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 247 ms: 1.27x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 258 ms: 1.25x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 541 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 462 ms: 1.15x faster                                                  |
| async_tree_io              | 668 ms                                                 | 580 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 460 ms: 1.14x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 68.8 ms                                                | 60.0 ms: 1.15x faster                                                 |
| float          | 55.8 ms                                                | 48.7 ms: 1.15x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 67.2 ms: 1.16x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.44 ms: 1.08x faster                                                 |
| regex_dna      | 154 ms                                                 | 145 ms: 1.07x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.4 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 181 us: 1.10x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 140 us: 1.07x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 52.7 ms: 1.06x faster                                                 |
| xml_etree_process    | 39.7 ms                                                | 37.6 ms: 1.06x faster                                                 |
| unpickle_list        | 3.02 us                                                | 2.92 us: 1.04x faster                                                 |
| json_loads           | 17.2 us                                                | 17.1 us: 1.01x faster                                                 |
| unpickle             | 9.12 us                                                | 9.24 us: 1.01x slower                                                 |
| pickle_dict          | 18.1 us                                                | 18.3 us: 1.01x slower                                                 |
| pickle_list          | 2.89 us                                                | 2.94 us: 1.02x slower                                                 |
| pickle               | 7.23 us                                                | 7.42 us: 1.03x slower                                                 |
| json_dumps           | 6.22 ms                                                | 6.43 ms: 1.03x slower                                                 |
| xml_etree_parse      | 106 ms                                                 | 110 ms: 1.04x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.48 sec: 1.06x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.8 ms: 1.47x slower                                                 |
| python_startup         | 11.4 ms                                                | 17.0 ms: 1.49x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.48x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 20.0 ms: 1.12x faster                                                 |
| mako            | 7.71 ms                                                | 6.93 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.5 us: 1.67x faster                                                 |
| deepcopy                   | 235 us                                                 | 145 us: 1.62x faster                                                  |
| generators                 | 31.1 ms                                                | 20.5 ms: 1.51x faster                                                 |
| raytrace                   | 212 ms                                                 | 149 ms: 1.42x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.51 us: 1.37x faster                                                 |
| async_tree_none_tg         | 258 ms                                                 | 189 ms: 1.36x faster                                                  |
| comprehensions             | 14.5 us                                                | 10.9 us: 1.34x faster                                                 |
| async_tree_none            | 266 ms                                                 | 199 ms: 1.34x faster                                                  |
| go                         | 102 ms                                                 | 79.2 ms: 1.28x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.12 ms: 1.28x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 247 ms: 1.27x faster                                                  |
| logging_silent             | 76.4 ns                                                | 60.7 ns: 1.26x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 258 ms: 1.25x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 541 ms: 1.24x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.02 us: 1.22x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.0 ms: 1.20x faster                                                 |
| unpack_sequence            | 31.5 ns                                                | 26.4 ns: 1.19x faster                                                 |
| chaos                      | 42.5 ms                                                | 35.8 ms: 1.19x faster                                                 |
| logging_format             | 3.98 us                                                | 3.35 us: 1.19x faster                                                 |
| nqueens                    | 62.4 ms                                                | 53.3 ms: 1.17x faster                                                 |
| regex_compile              | 77.9 ms                                                | 67.2 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 462 ms: 1.15x faster                                                  |
| async_tree_io              | 668 ms                                                 | 580 ms: 1.15x faster                                                  |
| nbody                      | 68.8 ms                                                | 60.0 ms: 1.15x faster                                                 |
| float                      | 55.8 ms                                                | 48.7 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 460 ms: 1.14x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 743 us: 1.14x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 67.0 ms: 1.14x faster                                                 |
| sympy_sum                  | 77.6 ms                                                | 68.4 ms: 1.13x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.77 ms: 1.13x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 905 us: 1.13x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 448 us: 1.13x faster                                                  |
| sympy_str                  | 148 ms                                                 | 131 ms: 1.12x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.05 ms: 1.12x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 67.8 ms: 1.12x faster                                                 |
| django_template            | 22.3 ms                                                | 20.0 ms: 1.12x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.42 sec: 1.11x faster                                                |
| mako                       | 7.71 ms                                                | 6.93 ms: 1.11x faster                                                 |
| sympy_integrate            | 11.4 ms                                                | 10.2 ms: 1.11x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 181 us: 1.10x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 27.2 ms: 1.10x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 169 ms: 1.10x faster                                                  |
| async_generators           | 304 ms                                                 | 278 ms: 1.09x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 31.4 ms: 1.08x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 460 ms: 1.08x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.44 ms: 1.08x faster                                                 |
| pprint_pformat             | 1.01 sec                                               | 938 ms: 1.08x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 140 us: 1.07x faster                                                  |
| docutils                   | 1.50 sec                                               | 1.40 sec: 1.07x faster                                                |
| regex_dna                  | 154 ms                                                 | 145 ms: 1.07x faster                                                  |
| scimark_fft                | 195 ms                                                 | 183 ms: 1.06x faster                                                  |
| pycparser                  | 677 ms                                                 | 637 ms: 1.06x faster                                                  |
| 2to3                       | 169 ms                                                 | 159 ms: 1.06x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 52.7 ms: 1.06x faster                                                 |
| sympy_expand               | 241 ms                                                 | 228 ms: 1.06x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 37.6 ms: 1.06x faster                                                 |
| richards_super             | 36.0 ms                                                | 34.2 ms: 1.05x faster                                                 |
| json                       | 3.09 ms                                                | 2.94 ms: 1.05x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 43.1 ms: 1.04x faster                                                 |
| unpickle_list              | 3.02 us                                                | 2.92 us: 1.04x faster                                                 |
| richards                   | 32.1 ms                                                | 31.1 ms: 1.03x faster                                                 |
| crypto_pyaes               | 51.9 ms                                                | 50.1 ms: 1.03x faster                                                 |
| pathlib                    | 24.2 ms                                                | 23.6 ms: 1.02x faster                                                 |
| sqlite_synth               | 1.57 us                                                | 1.55 us: 1.01x faster                                                 |
| json_loads                 | 17.2 us                                                | 17.1 us: 1.01x faster                                                 |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                  |
| meteor_contest             | 71.7 ms                                                | 71.8 ms: 1.00x slower                                                 |
| unpickle                   | 9.12 us                                                | 9.24 us: 1.01x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 94.4 us: 1.01x slower                                                 |
| pickle_dict                | 18.1 us                                                | 18.3 us: 1.01x slower                                                 |
| pyflate                    | 316 ms                                                 | 321 ms: 1.02x slower                                                  |
| pickle_list                | 2.89 us                                                | 2.94 us: 1.02x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.45 ms: 1.02x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.27 sec: 1.02x slower                                                |
| pickle                     | 7.23 us                                                | 7.42 us: 1.03x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 16.4 ms: 1.03x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.43 ms: 1.03x slower                                                 |
| xml_etree_parse            | 106 ms                                                 | 110 ms: 1.04x slower                                                  |
| fannkuch                   | 248 ms                                                 | 260 ms: 1.05x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.48 sec: 1.06x slower                                                |
| scimark_sor                | 87.4 ms                                                | 93.1 ms: 1.07x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 49.7 ms: 1.11x slower                                                 |
| coverage                   | 38.9 ms                                                | 44.0 ms: 1.13x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 895 us: 1.28x slower                                                  |
| telco                      | 3.68 ms                                                | 4.71 ms: 1.28x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 13.8 ms: 1.47x slower                                                 |
| python_startup             | 11.4 ms                                                | 17.0 ms: 1.49x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (4): asyncio_tcp, xml_etree_iterparse, pidigits, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.090x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.48x