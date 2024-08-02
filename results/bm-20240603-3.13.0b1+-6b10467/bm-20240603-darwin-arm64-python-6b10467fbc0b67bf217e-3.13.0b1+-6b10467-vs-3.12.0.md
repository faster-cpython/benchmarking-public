# Results vs. 3.12.0

- fork: python
- ref: 6b10467fbc0b67bf217e
- machine: darwin-arm64
- commit hash: 6b10467
- commit date: 2024-06-03
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.50x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 160 ms: 1.06x faster                                                   |
| chameleon      | 4.70 ms                                                | 4.27 ms: 1.10x faster                                                  |
| docutils       | 1.50 sec                                               | 1.43 sec: 1.05x faster                                                 |
| tornado_http   | 69.3 ms                                                | 65.4 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 237 ms: 1.36x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 196 ms: 1.32x faster                                                   |
| async_tree_none            | 266 ms                                                 | 208 ms: 1.28x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 256 ms: 1.22x faster                                                   |
| async_tree_io              | 668 ms                                                 | 550 ms: 1.21x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 554 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 450 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 465 ms: 1.13x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.8 ms: 1.14x faster                                                  |
| nbody          | 68.8 ms                                                | 60.8 ms: 1.13x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.2 ms: 1.14x faster                                                  |
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                                   |
| regex_effbot   | 2.64 ms                                                | 2.59 ms: 1.02x faster                                                  |
| regex_v8       | 16.0 ms                                                | 17.3 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 179 us: 1.12x faster                                                   |
| xml_etree_generate   | 55.8 ms                                                | 52.1 ms: 1.07x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 37.1 ms: 1.07x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 142 us: 1.06x faster                                                   |
| xml_etree_parse      | 106 ms                                                 | 102 ms: 1.04x faster                                                   |
| unpickle_list        | 3.02 us                                                | 2.90 us: 1.04x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 71.5 ms: 1.04x faster                                                  |
| json_loads           | 17.2 us                                                | 16.9 us: 1.02x faster                                                  |
| unpickle             | 9.12 us                                                | 9.23 us: 1.01x slower                                                  |
| pickle_dict          | 18.1 us                                                | 18.3 us: 1.01x slower                                                  |
| json_dumps           | 6.22 ms                                                | 6.36 ms: 1.02x slower                                                  |
| pickle               | 7.23 us                                                | 7.48 us: 1.04x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.45 sec: 1.04x slower                                                 |
| pickle_list          | 2.89 us                                                | 3.02 us: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 10.8 ms: 1.16x slower                                                  |
| python_startup         | 11.4 ms                                                | 13.8 ms: 1.21x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.3 ms: 1.16x faster                                                  |
| mako            | 7.71 ms                                                | 6.94 ms: 1.11x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| raytrace                   | 212 ms                                                 | 148 ms: 1.43x faster                                                   |
| generators                 | 31.1 ms                                                | 22.7 ms: 1.37x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 237 ms: 1.36x faster                                                   |
| comprehensions             | 14.5 us                                                | 10.9 us: 1.33x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 196 ms: 1.32x faster                                                   |
| async_tree_none            | 266 ms                                                 | 208 ms: 1.28x faster                                                   |
| deltablue                  | 2.71 ms                                                | 2.15 ms: 1.26x faster                                                  |
| logging_silent             | 76.4 ns                                                | 61.6 ns: 1.24x faster                                                  |
| chaos                      | 42.5 ms                                                | 34.6 ms: 1.23x faster                                                  |
| deepcopy_memo              | 27.7 us                                                | 22.6 us: 1.22x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 256 ms: 1.22x faster                                                   |
| async_tree_io              | 668 ms                                                 | 550 ms: 1.21x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 554 ms: 1.21x faster                                                   |
| logging_simple             | 3.69 us                                                | 3.07 us: 1.20x faster                                                  |
| coroutines                 | 19.2 ms                                                | 16.0 ms: 1.20x faster                                                  |
| logging_format             | 3.98 us                                                | 3.36 us: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 450 ms: 1.18x faster                                                   |
| nqueens                    | 62.4 ms                                                | 52.8 ms: 1.18x faster                                                  |
| django_template            | 22.3 ms                                                | 19.3 ms: 1.16x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 736 us: 1.15x faster                                                   |
| deepcopy_reduce            | 2.07 us                                                | 1.80 us: 1.15x faster                                                  |
| deepcopy                   | 235 us                                                 | 204 us: 1.15x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 66.6 ms: 1.15x faster                                                  |
| float                      | 55.8 ms                                                | 48.8 ms: 1.14x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 66.6 ms: 1.14x faster                                                  |
| regex_compile              | 77.9 ms                                                | 68.2 ms: 1.14x faster                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 896 us: 1.14x faster                                                   |
| nbody                      | 68.8 ms                                                | 60.8 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 465 ms: 1.13x faster                                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.78 ms: 1.13x faster                                                  |
| sympy_str                  | 148 ms                                                 | 132 ms: 1.12x faster                                                   |
| sympy_sum                  | 77.6 ms                                                | 69.4 ms: 1.12x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 179 us: 1.12x faster                                                   |
| sqlglot_normalize          | 186 ms                                                 | 167 ms: 1.11x faster                                                   |
| hexiom                     | 4.54 ms                                                | 4.09 ms: 1.11x faster                                                  |
| mako                       | 7.71 ms                                                | 6.94 ms: 1.11x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 10.3 ms: 1.10x faster                                                  |
| chameleon                  | 4.70 ms                                                | 4.27 ms: 1.10x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.1 ms: 1.10x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 31.0 ms: 1.10x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 460 us: 1.10x faster                                                   |
| dulwich_log                | 29.8 ms                                                | 27.4 ms: 1.09x faster                                                  |
| asyncio_tcp                | 449 ms                                                 | 412 ms: 1.09x faster                                                   |
| async_generators           | 304 ms                                                 | 281 ms: 1.08x faster                                                   |
| aiohttp                    | 1.08 ms                                                | 1.00 ms: 1.08x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 941 ms: 1.07x faster                                                   |
| pprint_safe_repr           | 497 ms                                                 | 463 ms: 1.07x faster                                                   |
| scimark_fft                | 195 ms                                                 | 182 ms: 1.07x faster                                                   |
| xml_etree_generate         | 55.8 ms                                                | 52.1 ms: 1.07x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 37.1 ms: 1.07x faster                                                  |
| sympy_expand               | 241 ms                                                 | 226 ms: 1.07x faster                                                   |
| gunicorn                   | 1.15 ms                                                | 1.08 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 142 us: 1.06x faster                                                   |
| tornado_http               | 69.3 ms                                                | 65.4 ms: 1.06x faster                                                  |
| pycparser                  | 677 ms                                                 | 639 ms: 1.06x faster                                                   |
| 2to3                       | 169 ms                                                 | 160 ms: 1.06x faster                                                   |
| scimark_monte_carlo        | 45.0 ms                                                | 42.6 ms: 1.06x faster                                                  |
| json                       | 3.09 ms                                                | 2.93 ms: 1.05x faster                                                  |
| docutils                   | 1.50 sec                                               | 1.43 sec: 1.05x faster                                                 |
| xml_etree_parse            | 106 ms                                                 | 102 ms: 1.04x faster                                                   |
| unpickle_list              | 3.02 us                                                | 2.90 us: 1.04x faster                                                  |
| crypto_pyaes               | 51.9 ms                                                | 50.0 ms: 1.04x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 71.5 ms: 1.04x faster                                                  |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                                   |
| richards_super             | 36.0 ms                                                | 35.0 ms: 1.03x faster                                                  |
| dask                       | 222 ms                                                 | 217 ms: 1.02x faster                                                   |
| meteor_contest             | 71.7 ms                                                | 70.1 ms: 1.02x faster                                                  |
| sqlite_synth               | 1.57 us                                                | 1.53 us: 1.02x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.54 sec: 1.02x faster                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 91.0 us: 1.02x faster                                                  |
| json_loads                 | 17.2 us                                                | 16.9 us: 1.02x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.59 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.23 sec: 1.01x faster                                                 |
| go                         | 102 ms                                                 | 100 ms: 1.01x faster                                                   |
| richards                   | 32.1 ms                                                | 31.9 ms: 1.01x faster                                                  |
| fannkuch                   | 248 ms                                                 | 248 ms: 1.00x faster                                                   |
| pyflate                    | 316 ms                                                 | 318 ms: 1.01x slower                                                   |
| unpickle                   | 9.12 us                                                | 9.23 us: 1.01x slower                                                  |
| pickle_dict                | 18.1 us                                                | 18.3 us: 1.01x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.45 ms: 1.02x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 6.36 ms: 1.02x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 46.0 ms: 1.02x slower                                                  |
| pickle                     | 7.23 us                                                | 7.48 us: 1.04x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.45 sec: 1.04x slower                                                 |
| pickle_list                | 2.89 us                                                | 3.02 us: 1.05x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 94.8 ms: 1.09x slower                                                  |
| regex_v8                   | 16.0 ms                                                | 17.3 ms: 1.09x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 10.8 ms: 1.16x slower                                                  |
| coverage                   | 38.9 ms                                                | 44.9 ms: 1.16x slower                                                  |
| python_startup             | 11.4 ms                                                | 13.8 ms: 1.21x slower                                                  |
| telco                      | 3.68 ms                                                | 4.53 ms: 1.23x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 892 us: 1.27x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (3): mypy2, asyncio_websockets, pidigits
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (14) of results/bm-20240603-3.13.0b1+-6b10467/bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.50x