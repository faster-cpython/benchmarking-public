# Results vs. 3.12.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: darwin-arm64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 161 ms: 1.05x faster                                                  |
| docutils       | 1.50 sec                                               | 1.43 sec: 1.05x faster                                                |
| tornado_http   | 69.3 ms                                                | 82.2 ms: 1.19x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 185 ms: 1.39x faster                                                  |
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 246 ms: 1.27x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 255 ms: 1.26x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 536 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 459 ms: 1.16x faster                                                  |
| async_tree_io              | 668 ms                                                 | 579 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 459 ms: 1.15x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.4 ms: 1.15x faster                                                 |
| nbody          | 68.8 ms                                                | 60.1 ms: 1.15x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 67.2 ms: 1.16x faster                                                 |
| regex_dna      | 154 ms                                                 | 146 ms: 1.05x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.53 ms: 1.04x faster                                                 |
| regex_v8       | 16.0 ms                                                | 16.8 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 182 us: 1.10x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 141 us: 1.07x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 52.6 ms: 1.06x faster                                                 |
| xml_etree_process    | 39.7 ms                                                | 37.5 ms: 1.06x faster                                                 |
| unpickle_list        | 3.02 us                                                | 2.94 us: 1.03x faster                                                 |
| json_loads           | 17.2 us                                                | 16.8 us: 1.02x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 73.7 ms: 1.00x faster                                                 |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| xml_etree_parse      | 106 ms                                                 | 107 ms: 1.01x slower                                                  |
| json_dumps           | 6.22 ms                                                | 6.31 ms: 1.01x slower                                                 |
| pickle               | 7.23 us                                                | 7.39 us: 1.02x slower                                                 |
| pickle_list          | 2.89 us                                                | 2.99 us: 1.04x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 1.47 sec: 1.06x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 11.0 ms: 1.17x slower                                                 |
| python_startup         | 11.4 ms                                                | 13.9 ms: 1.22x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.19x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 20.1 ms: 1.11x faster                                                 |
| mako            | 7.71 ms                                                | 7.06 ms: 1.09x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.7 us: 1.65x faster                                                 |
| deepcopy                   | 235 us                                                 | 146 us: 1.61x faster                                                  |
| generators                 | 31.1 ms                                                | 20.7 ms: 1.50x faster                                                 |
| raytrace                   | 212 ms                                                 | 149 ms: 1.42x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 185 ms: 1.39x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.50 us: 1.38x faster                                                 |
| async_tree_none            | 266 ms                                                 | 198 ms: 1.34x faster                                                  |
| comprehensions             | 14.5 us                                                | 10.9 us: 1.34x faster                                                 |
| go                         | 102 ms                                                 | 79.1 ms: 1.28x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 246 ms: 1.27x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 255 ms: 1.26x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.14 ms: 1.26x faster                                                 |
| logging_silent             | 76.4 ns                                                | 60.9 ns: 1.26x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 536 ms: 1.25x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.02 us: 1.22x faster                                                 |
| logging_format             | 3.98 us                                                | 3.32 us: 1.20x faster                                                 |
| chaos                      | 42.5 ms                                                | 35.6 ms: 1.19x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.19x faster                                                 |
| unpack_sequence            | 31.5 ns                                                | 26.6 ns: 1.18x faster                                                 |
| nqueens                    | 62.4 ms                                                | 53.2 ms: 1.17x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 64.8 ms: 1.17x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.70 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 459 ms: 1.16x faster                                                  |
| regex_compile              | 77.9 ms                                                | 67.2 ms: 1.16x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 66.0 ms: 1.16x faster                                                 |
| async_tree_io              | 668 ms                                                 | 579 ms: 1.15x faster                                                  |
| float                      | 55.8 ms                                                | 48.4 ms: 1.15x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 737 us: 1.15x faster                                                  |
| nbody                      | 68.8 ms                                                | 60.1 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 459 ms: 1.15x faster                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 900 us: 1.13x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 68.8 ms: 1.13x faster                                                 |
| hexiom                     | 4.54 ms                                                | 4.05 ms: 1.12x faster                                                 |
| sympy_str                  | 148 ms                                                 | 131 ms: 1.12x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 452 us: 1.12x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 167 ms: 1.11x faster                                                  |
| django_template            | 22.3 ms                                                | 20.1 ms: 1.11x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.43 sec: 1.11x faster                                                |
| sympy_integrate            | 11.4 ms                                                | 10.3 ms: 1.10x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 27.1 ms: 1.10x faster                                                 |
| asyncio_tcp                | 449 ms                                                 | 409 ms: 1.10x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 182 us: 1.10x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 31.0 ms: 1.10x faster                                                 |
| mako                       | 7.71 ms                                                | 7.06 ms: 1.09x faster                                                 |
| async_generators           | 304 ms                                                 | 278 ms: 1.09x faster                                                  |
| scimark_fft                | 195 ms                                                 | 179 ms: 1.09x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 458 ms: 1.09x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 932 ms: 1.09x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 141 us: 1.07x faster                                                  |
| sympy_expand               | 241 ms                                                 | 226 ms: 1.07x faster                                                  |
| json                       | 3.09 ms                                                | 2.91 ms: 1.06x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 52.6 ms: 1.06x faster                                                 |
| pycparser                  | 677 ms                                                 | 639 ms: 1.06x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 37.5 ms: 1.06x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 42.6 ms: 1.06x faster                                                 |
| regex_dna                  | 154 ms                                                 | 146 ms: 1.05x faster                                                  |
| 2to3                       | 169 ms                                                 | 161 ms: 1.05x faster                                                  |
| docutils                   | 1.50 sec                                               | 1.43 sec: 1.05x faster                                                |
| regex_effbot               | 2.64 ms                                                | 2.53 ms: 1.04x faster                                                 |
| crypto_pyaes               | 51.9 ms                                                | 50.2 ms: 1.03x faster                                                 |
| unpickle_list              | 3.02 us                                                | 2.94 us: 1.03x faster                                                 |
| pathlib                    | 24.2 ms                                                | 23.6 ms: 1.03x faster                                                 |
| json_loads                 | 17.2 us                                                | 16.8 us: 1.02x faster                                                 |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 92.2 us: 1.01x faster                                                 |
| richards_super             | 36.0 ms                                                | 35.9 ms: 1.00x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 73.7 ms: 1.00x faster                                                 |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                  |
| richards                   | 32.1 ms                                                | 32.0 ms: 1.00x faster                                                 |
| meteor_contest             | 71.7 ms                                                | 71.6 ms: 1.00x faster                                                 |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| xml_etree_parse            | 106 ms                                                 | 107 ms: 1.01x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 6.31 ms: 1.01x slower                                                 |
| pyflate                    | 316 ms                                                 | 320 ms: 1.01x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.45 ms: 1.02x slower                                                 |
| pickle                     | 7.23 us                                                | 7.39 us: 1.02x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.28 sec: 1.03x slower                                                |
| pickle_list                | 2.89 us                                                | 2.99 us: 1.04x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 16.8 ms: 1.05x slower                                                 |
| fannkuch                   | 248 ms                                                 | 262 ms: 1.06x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.47 sec: 1.06x slower                                                |
| scimark_sor                | 87.4 ms                                                | 93.1 ms: 1.07x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 48.1 ms: 1.07x slower                                                 |
| coverage                   | 38.9 ms                                                | 44.3 ms: 1.14x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 11.0 ms: 1.17x slower                                                 |
| tornado_http               | 69.3 ms                                                | 82.2 ms: 1.19x slower                                                 |
| python_startup             | 11.4 ms                                                | 13.9 ms: 1.22x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 901 us: 1.28x slower                                                  |
| telco                      | 3.68 ms                                                | 4.74 ms: 1.29x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (2): unpickle, pidigits
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.51x