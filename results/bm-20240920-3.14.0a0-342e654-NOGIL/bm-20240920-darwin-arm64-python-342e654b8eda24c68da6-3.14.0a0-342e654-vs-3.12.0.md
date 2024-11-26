# Results vs. 3.12.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: darwin-arm64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.237x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x slower
- Memory change: 0.79x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 246 ms: 1.45x slower                                                  |
| docutils       | 1.50 sec                                               | 1.75 sec: 1.16x slower                                                |
| tornado_http   | 69.3 ms                                                | 127 ms: 1.83x slower                                                  |
| Geometric mean | (ref)                                                  | 1.46x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 499 ms: 1.34x faster                                                  |
| async_tree_io              | 668 ms                                                 | 525 ms: 1.27x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 206 ms: 1.25x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 263 ms: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 460 ms: 1.16x faster                                                  |
| async_tree_none            | 266 ms                                                 | 233 ms: 1.14x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 288 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 485 ms: 1.08x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| float          | 55.8 ms                                                | 93.8 ms: 1.68x slower                                                 |
| nbody          | 68.8 ms                                                | 154 ms: 2.24x slower                                                  |
| Geometric mean | (ref)                                                  | 1.55x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 139 ms: 1.11x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.44 ms: 1.08x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.1 ms: 1.07x slower                                                 |
| regex_compile  | 77.9 ms                                                | 119 ms: 1.53x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle               | 7.23 us                                                | 7.05 us: 1.03x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 104 ms: 1.02x faster                                                  |
| pickle_list          | 2.89 us                                                | 2.90 us: 1.01x slower                                                 |
| pickle_dict          | 18.1 us                                                | 18.4 us: 1.02x slower                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 75.6 ms: 1.02x slower                                                 |
| unpickle             | 9.12 us                                                | 9.72 us: 1.07x slower                                                 |
| unpickle_list        | 3.02 us                                                | 3.25 us: 1.07x slower                                                 |
| json_loads           | 17.2 us                                                | 18.8 us: 1.09x slower                                                 |
| xml_etree_generate   | 55.8 ms                                                | 68.1 ms: 1.22x slower                                                 |
| json_dumps           | 6.22 ms                                                | 7.74 ms: 1.24x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 1.99 sec: 1.43x slower                                                |
| xml_etree_process    | 39.7 ms                                                | 57.2 ms: 1.44x slower                                                 |
| pickle_pure_python   | 200 us                                                 | 346 us: 1.73x slower                                                  |
| unpickle_pure_python | 151 us                                                 | 262 us: 1.74x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.6 ms: 1.45x slower                                                 |
| python_startup         | 11.4 ms                                                | 17.0 ms: 1.49x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.47x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 35.3 ms: 1.58x slower                                                 |
| mako            | 7.71 ms                                                | 13.3 ms: 1.73x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.65x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| sqlglot_normalize          | 186 ms                                                 | 102 ms: 1.82x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 499 ms: 1.34x faster                                                  |
| asyncio_tcp                | 449 ms                                                 | 335 ms: 1.34x faster                                                  |
| async_tree_io              | 668 ms                                                 | 525 ms: 1.27x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 206 ms: 1.25x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 263 ms: 1.23x faster                                                  |
| gc_traversal               | 2.40 ms                                                | 2.05 ms: 1.17x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 460 ms: 1.16x faster                                                  |
| async_tree_none            | 266 ms                                                 | 233 ms: 1.14x faster                                                  |
| regex_dna                  | 154 ms                                                 | 139 ms: 1.11x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 288 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 485 ms: 1.08x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.44 ms: 1.08x faster                                                 |
| pickle                     | 7.23 us                                                | 7.05 us: 1.03x faster                                                 |
| sqlite_synth               | 1.57 us                                                | 1.53 us: 1.02x faster                                                 |
| create_gc_cycles           | 701 us                                                 | 686 us: 1.02x faster                                                  |
| xml_etree_parse            | 106 ms                                                 | 104 ms: 1.02x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 405 ms: 1.01x faster                                                  |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| pickle_list                | 2.89 us                                                | 2.90 us: 1.01x slower                                                 |
| pickle_dict                | 18.1 us                                                | 18.4 us: 1.02x slower                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 75.6 ms: 1.02x slower                                                 |
| deepcopy                   | 235 us                                                 | 245 us: 1.04x slower                                                  |
| pathlib                    | 24.2 ms                                                | 25.6 ms: 1.06x slower                                                 |
| unpickle                   | 9.12 us                                                | 9.72 us: 1.07x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.1 ms: 1.07x slower                                                 |
| unpickle_list              | 3.02 us                                                | 3.25 us: 1.07x slower                                                 |
| json                       | 3.09 ms                                                | 3.35 ms: 1.09x slower                                                 |
| async_generators           | 304 ms                                                 | 331 ms: 1.09x slower                                                  |
| json_loads                 | 17.2 us                                                | 18.8 us: 1.09x slower                                                 |
| generators                 | 31.1 ms                                                | 34.6 ms: 1.11x slower                                                 |
| deepcopy_memo              | 27.7 us                                                | 31.2 us: 1.13x slower                                                 |
| mdp                        | 1.58 sec                                               | 1.83 sec: 1.16x slower                                                |
| docutils                   | 1.50 sec                                               | 1.75 sec: 1.16x slower                                                |
| deepcopy_reduce            | 2.07 us                                                | 2.46 us: 1.19x slower                                                 |
| nqueens                    | 62.4 ms                                                | 75.5 ms: 1.21x slower                                                 |
| xml_etree_generate         | 55.8 ms                                                | 68.1 ms: 1.22x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 54.9 ms: 1.22x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 88.7 ms: 1.24x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 7.74 ms: 1.24x slower                                                 |
| comprehensions             | 14.5 us                                                | 18.7 us: 1.29x slower                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 4.06 ms: 1.29x slower                                                 |
| coroutines                 | 19.2 ms                                                | 25.0 ms: 1.30x slower                                                 |
| scimark_fft                | 195 ms                                                 | 263 ms: 1.35x slower                                                  |
| pycparser                  | 677 ms                                                 | 913 ms: 1.35x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 15.4 ms: 1.35x slower                                                 |
| dulwich_log                | 29.8 ms                                                | 40.7 ms: 1.36x slower                                                 |
| fannkuch                   | 248 ms                                                 | 352 ms: 1.42x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.99 sec: 1.43x slower                                                |
| coverage                   | 38.9 ms                                                | 55.6 ms: 1.43x slower                                                 |
| xml_etree_process          | 39.7 ms                                                | 57.2 ms: 1.44x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 13.6 ms: 1.45x slower                                                 |
| 2to3                       | 169 ms                                                 | 246 ms: 1.45x slower                                                  |
| python_startup             | 11.4 ms                                                | 17.0 ms: 1.49x slower                                                 |
| crypto_pyaes               | 51.9 ms                                                | 77.4 ms: 1.49x slower                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 50.9 ms: 1.50x slower                                                 |
| pyflate                    | 316 ms                                                 | 479 ms: 1.52x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 142 us: 1.53x slower                                                  |
| regex_compile              | 77.9 ms                                                | 119 ms: 1.53x slower                                                  |
| sympy_str                  | 148 ms                                                 | 227 ms: 1.54x slower                                                  |
| spectral_norm              | 76.4 ms                                                | 118 ms: 1.54x slower                                                  |
| telco                      | 3.68 ms                                                | 5.69 ms: 1.55x slower                                                 |
| bench_thread_pool          | 504 us                                                 | 792 us: 1.57x slower                                                  |
| django_template            | 22.3 ms                                                | 35.3 ms: 1.58x slower                                                 |
| pprint_pformat             | 1.01 sec                                               | 1.64 sec: 1.63x slower                                                |
| pprint_safe_repr           | 497 ms                                                 | 808 ms: 1.63x slower                                                  |
| logging_simple             | 3.69 us                                                | 6.05 us: 1.64x slower                                                 |
| logging_format             | 3.98 us                                                | 6.60 us: 1.66x slower                                                 |
| hexiom                     | 4.54 ms                                                | 7.63 ms: 1.68x slower                                                 |
| float                      | 55.8 ms                                                | 93.8 ms: 1.68x slower                                                 |
| mako                       | 7.71 ms                                                | 13.3 ms: 1.73x slower                                                 |
| richards                   | 32.1 ms                                                | 55.6 ms: 1.73x slower                                                 |
| pickle_pure_python         | 200 us                                                 | 346 us: 1.73x slower                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 78.1 ms: 1.73x slower                                                 |
| unpickle_pure_python       | 151 us                                                 | 262 us: 1.74x slower                                                  |
| chaos                      | 42.5 ms                                                | 74.2 ms: 1.74x slower                                                 |
| sympy_expand               | 241 ms                                                 | 421 ms: 1.74x slower                                                  |
| raytrace                   | 212 ms                                                 | 373 ms: 1.76x slower                                                  |
| sympy_sum                  | 77.6 ms                                                | 137 ms: 1.77x slower                                                  |
| logging_silent             | 76.4 ns                                                | 135 ns: 1.77x slower                                                  |
| richards_super             | 36.0 ms                                                | 64.3 ms: 1.78x slower                                                 |
| go                         | 102 ms                                                 | 181 ms: 1.78x slower                                                  |
| tornado_http               | 69.3 ms                                                | 127 ms: 1.83x slower                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.88 ms: 1.84x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 165 ms: 1.89x slower                                                  |
| scimark_lu                 | 76.0 ms                                                | 144 ms: 1.90x slower                                                  |
| sqlglot_parse              | 848 us                                                 | 1.64 ms: 1.94x slower                                                 |
| deltablue                  | 2.71 ms                                                | 5.63 ms: 2.08x slower                                                 |
| nbody                      | 68.8 ms                                                | 154 ms: 2.24x slower                                                  |
| unpack_sequence            | 31.5 ns                                                | 96.0 ns: 3.05x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.30x slower                                                          |

Benchmark hidden because not significant (1): asyncio_tcp_ssl
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20240920-3.14.0a0-342e654-NOGIL/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.237x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.23x
- 95% likely to have a slowdown of 1.20x
- 99% likely to have a slowdown of 1.16x

# Memory
- memory change: 0.79x