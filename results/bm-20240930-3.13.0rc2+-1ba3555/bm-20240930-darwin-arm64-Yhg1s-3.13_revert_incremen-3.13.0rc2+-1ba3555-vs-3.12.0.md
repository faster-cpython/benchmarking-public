# Results vs. 3.12.0

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: darwin-arm64
- commit hash: 1ba3555
- commit date: 2024-09-30
- overall geometric mean: 1.00x faster
- HPT reliability: 63.36%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 174 ms: 1.03x slower                                                   |
| chameleon      | 4.70 ms                                                | 4.75 ms: 1.01x slower                                                  |
| docutils       | 1.50 sec                                               | 1.43 sec: 1.05x faster                                                 |
| tornado_http   | 69.3 ms                                                | 82.8 ms: 1.20x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 494 ms: 1.35x faster                                                   |
| async_tree_io              | 668 ms                                                 | 501 ms: 1.33x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 194 ms: 1.32x faster                                                   |
| async_tree_none            | 266 ms                                                 | 210 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 442 ms: 1.20x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 264 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 454 ms: 1.16x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 285 ms: 1.13x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 54.6 ms: 1.02x faster                                                  |
| nbody          | 68.8 ms                                                | 75.1 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                                   |
| regex_effbot   | 2.64 ms                                                | 2.58 ms: 1.02x faster                                                  |
| regex_compile  | 77.9 ms                                                | 76.1 ms: 1.02x faster                                                  |
| regex_v8       | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_list        | 3.02 us                                                | 2.86 us: 1.05x faster                                                  |
| json_loads           | 17.2 us                                                | 16.9 us: 1.02x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 56.3 ms: 1.01x slower                                                  |
| unpickle             | 9.12 us                                                | 9.21 us: 1.01x slower                                                  |
| pickle_dict          | 18.1 us                                                | 18.3 us: 1.01x slower                                                  |
| pickle_pure_python   | 200 us                                                 | 203 us: 1.02x slower                                                   |
| xml_etree_process    | 39.7 ms                                                | 40.8 ms: 1.03x slower                                                  |
| unpickle_pure_python | 151 us                                                 | 156 us: 1.03x slower                                                   |
| pickle_list          | 2.89 us                                                | 3.03 us: 1.05x slower                                                  |
| pickle               | 7.23 us                                                | 7.60 us: 1.05x slower                                                  |
| json_dumps           | 6.22 ms                                                | 6.56 ms: 1.05x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.52 sec: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.2 ms: 1.41x slower                                                  |
| python_startup         | 11.4 ms                                                | 16.7 ms: 1.46x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.44x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 7.54 ms: 1.02x faster                                                  |
| django_template | 22.3 ms                                                | 22.1 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 494 ms: 1.35x faster                                                   |
| async_tree_io              | 668 ms                                                 | 501 ms: 1.33x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 194 ms: 1.32x faster                                                   |
| async_tree_none            | 266 ms                                                 | 210 ms: 1.26x faster                                                   |
| raytrace                   | 212 ms                                                 | 173 ms: 1.22x faster                                                   |
| generators                 | 31.1 ms                                                | 25.4 ms: 1.22x faster                                                  |
| comprehensions             | 14.5 us                                                | 12.0 us: 1.21x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 442 ms: 1.20x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 264 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 454 ms: 1.16x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 285 ms: 1.13x faster                                                   |
| deltablue                  | 2.71 ms                                                | 2.46 ms: 1.10x faster                                                  |
| logging_silent             | 76.4 ns                                                | 69.5 ns: 1.10x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.92 ms: 1.07x faster                                                  |
| chaos                      | 42.5 ms                                                | 39.6 ms: 1.07x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.47 sec: 1.07x faster                                                 |
| deepcopy_memo              | 27.7 us                                                | 25.9 us: 1.07x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.47 us: 1.06x faster                                                  |
| logging_format             | 3.98 us                                                | 3.75 us: 1.06x faster                                                  |
| unpickle_list              | 3.02 us                                                | 2.86 us: 1.05x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 72.5 ms: 1.05x faster                                                  |
| docutils                   | 1.50 sec                                               | 1.43 sec: 1.05x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 479 us: 1.05x faster                                                   |
| nqueens                    | 62.4 ms                                                | 59.6 ms: 1.05x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 28.6 ms: 1.04x faster                                                  |
| coroutines                 | 19.2 ms                                                | 18.5 ms: 1.04x faster                                                  |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                                   |
| sympy_sum                  | 77.6 ms                                                | 75.4 ms: 1.03x faster                                                  |
| deepcopy                   | 235 us                                                 | 228 us: 1.03x faster                                                   |
| async_generators           | 304 ms                                                 | 296 ms: 1.03x faster                                                   |
| json                       | 3.09 ms                                                | 3.01 ms: 1.03x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 2.02 us: 1.03x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.58 ms: 1.02x faster                                                  |
| regex_compile              | 77.9 ms                                                | 76.1 ms: 1.02x faster                                                  |
| sympy_str                  | 148 ms                                                 | 144 ms: 1.02x faster                                                   |
| mako                       | 7.71 ms                                                | 7.54 ms: 1.02x faster                                                  |
| json_loads                 | 17.2 us                                                | 16.9 us: 1.02x faster                                                  |
| float                      | 55.8 ms                                                | 54.6 ms: 1.02x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 11.2 ms: 1.01x faster                                                  |
| django_template            | 22.3 ms                                                | 22.1 ms: 1.01x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 838 us: 1.01x faster                                                   |
| sqlglot_transpile          | 1.02 ms                                                | 1.01 ms: 1.01x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                   |
| scimark_fft                | 195 ms                                                 | 197 ms: 1.01x slower                                                   |
| xml_etree_generate         | 55.8 ms                                                | 56.3 ms: 1.01x slower                                                  |
| sqlglot_normalize          | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| unpickle                   | 9.12 us                                                | 9.21 us: 1.01x slower                                                  |
| chameleon                  | 4.70 ms                                                | 4.75 ms: 1.01x slower                                                  |
| scimark_lu                 | 76.0 ms                                                | 76.9 ms: 1.01x slower                                                  |
| pickle_dict                | 18.1 us                                                | 18.3 us: 1.01x slower                                                  |
| pickle_pure_python         | 200 us                                                 | 203 us: 1.02x slower                                                   |
| meteor_contest             | 71.7 ms                                                | 73.3 ms: 1.02x slower                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 34.8 ms: 1.02x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.02x slower                                                  |
| sympy_expand               | 241 ms                                                 | 247 ms: 1.03x slower                                                   |
| 2to3                       | 169 ms                                                 | 174 ms: 1.03x slower                                                   |
| xml_etree_process          | 39.7 ms                                                | 40.8 ms: 1.03x slower                                                  |
| pycparser                  | 677 ms                                                 | 698 ms: 1.03x slower                                                   |
| unpickle_pure_python       | 151 us                                                 | 156 us: 1.03x slower                                                   |
| crypto_pyaes               | 51.9 ms                                                | 53.6 ms: 1.03x slower                                                  |
| hexiom                     | 4.54 ms                                                | 4.70 ms: 1.03x slower                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.03x slower                                                 |
| dask                       | 222 ms                                                 | 230 ms: 1.04x slower                                                   |
| pprint_safe_repr           | 497 ms                                                 | 516 ms: 1.04x slower                                                   |
| pprint_pformat             | 1.01 sec                                               | 1.05 sec: 1.04x slower                                                 |
| pickle_list                | 2.89 us                                                | 3.03 us: 1.05x slower                                                  |
| pickle                     | 7.23 us                                                | 7.60 us: 1.05x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 6.56 ms: 1.05x slower                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 47.7 ms: 1.06x slower                                                  |
| richards_super             | 36.0 ms                                                | 38.4 ms: 1.06x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 99.2 us: 1.07x slower                                                  |
| aiohttp                    | 1.08 ms                                                | 1.16 ms: 1.07x slower                                                  |
| fannkuch                   | 248 ms                                                 | 267 ms: 1.08x slower                                                   |
| richards                   | 32.1 ms                                                | 34.6 ms: 1.08x slower                                                  |
| pyflate                    | 316 ms                                                 | 341 ms: 1.08x slower                                                   |
| go                         | 102 ms                                                 | 110 ms: 1.09x slower                                                   |
| tomli_loads                | 1.39 sec                                               | 1.52 sec: 1.09x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                  |
| nbody                      | 68.8 ms                                                | 75.1 ms: 1.09x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 50.7 ms: 1.13x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 808 us: 1.15x slower                                                   |
| scimark_sor                | 87.4 ms                                                | 103 ms: 1.18x slower                                                   |
| coverage                   | 38.9 ms                                                | 46.1 ms: 1.19x slower                                                  |
| tornado_http               | 69.3 ms                                                | 82.8 ms: 1.20x slower                                                  |
| mypy2                      | 380 ms                                                 | 484 ms: 1.27x slower                                                   |
| telco                      | 3.68 ms                                                | 4.77 ms: 1.30x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 13.2 ms: 1.41x slower                                                  |
| python_startup             | 11.4 ms                                                | 16.7 ms: 1.46x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (8): sqlite_synth, xml_etree_iterparse, pidigits, unpack_sequence, xml_etree_parse, pathlib, asyncio_tcp, gunicorn
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (15) of results/bm-20240930-3.13.0rc2+-1ba3555/bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 63.36% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.51x