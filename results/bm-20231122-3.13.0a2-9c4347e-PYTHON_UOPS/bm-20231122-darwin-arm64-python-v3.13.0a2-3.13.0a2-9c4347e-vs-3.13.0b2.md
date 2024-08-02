# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a2
- machine: darwin-arm64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.14x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 179 ms: 1.11x slower                                       |
| chameleon      | 4.27 ms                                                    | 4.93 ms: 1.15x slower                                      |
| docutils       | 1.44 sec                                                   | 1.51 sec: 1.05x slower                                     |
| tornado_http   | 66.7 ms                                                    | 71.4 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                      | 1.10x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 467 ms                                                     | 532 ms: 1.14x slower                                       |
| async_tree_cpu_io_mixed_tg | 451 ms                                                     | 549 ms: 1.22x slower                                       |
| async_tree_io_tg           | 565 ms                                                     | 703 ms: 1.24x slower                                       |
| async_tree_none            | 209 ms                                                     | 263 ms: 1.26x slower                                       |
| async_tree_io              | 563 ms                                                     | 719 ms: 1.28x slower                                       |
| async_tree_memoization     | 260 ms                                                     | 339 ms: 1.31x slower                                       |
| async_tree_none_tg         | 198 ms                                                     | 277 ms: 1.40x slower                                       |
| async_tree_memoization_tg  | 240 ms                                                     | 346 ms: 1.45x slower                                       |
| Geometric mean             | (ref)                                                      | 1.28x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 284 ms: 1.01x slower                                       |
| float          | 48.6 ms                                                    | 68.2 ms: 1.40x slower                                      |
| nbody          | 59.6 ms                                                    | 86.3 ms: 1.45x slower                                      |
| Geometric mean | (ref)                                                      | 1.27x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                      |
| regex_v8       | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                      |
| regex_dna      | 149 ms                                                     | 155 ms: 1.04x slower                                       |
| regex_compile  | 68.5 ms                                                    | 85.5 ms: 1.25x slower                                      |
| Geometric mean | (ref)                                                      | 1.07x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pickle               | 7.48 us                                                    | 7.36 us: 1.02x faster                                      |
| unpickle             | 9.12 us                                                    | 8.99 us: 1.01x faster                                      |
| pickle_dict          | 18.3 us                                                    | 18.1 us: 1.01x faster                                      |
| pickle_list          | 2.96 us                                                    | 2.93 us: 1.01x faster                                      |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.01x slower                                       |
| json_loads           | 16.8 us                                                    | 17.1 us: 1.01x slower                                      |
| unpickle_list        | 2.88 us                                                    | 2.98 us: 1.03x slower                                      |
| json_dumps           | 6.23 ms                                                    | 6.61 ms: 1.06x slower                                      |
| xml_etree_process    | 37.1 ms                                                    | 41.2 ms: 1.11x slower                                      |
| pickle_pure_python   | 179 us                                                     | 201 us: 1.12x slower                                       |
| xml_etree_generate   | 52.7 ms                                                    | 59.6 ms: 1.13x slower                                      |
| xml_etree_iterparse  | 71.5 ms                                                    | 81.1 ms: 1.13x slower                                      |
| tomli_loads          | 1.47 sec                                                   | 1.67 sec: 1.14x slower                                     |
| unpickle_pure_python | 141 us                                                     | 168 us: 1.19x slower                                       |
| Geometric mean       | (ref)                                                      | 1.06x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 12.7 ms: 1.20x faster                                      |
| python_startup_no_site | 12.3 ms                                                    | 11.4 ms: 1.08x faster                                      |
| Geometric mean         | (ref)                                                      | 1.14x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 6.99 ms                                                    | 9.60 ms: 1.37x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 897 us                                                     | 704 us: 1.27x faster                                       |
| python_startup             | 15.2 ms                                                    | 12.7 ms: 1.20x faster                                      |
| typing_runtime_protocols   | 87.6 us                                                    | 77.1 us: 1.14x faster                                      |
| python_startup_no_site     | 12.3 ms                                                    | 11.4 ms: 1.08x faster                                      |
| bench_mp_pool              | 47.2 ms                                                    | 44.8 ms: 1.05x faster                                      |
| gc_traversal               | 2.45 ms                                                    | 2.40 ms: 1.02x faster                                      |
| pickle                     | 7.48 us                                                    | 7.36 us: 1.02x faster                                      |
| unpickle                   | 9.12 us                                                    | 8.99 us: 1.01x faster                                      |
| pickle_dict                | 18.3 us                                                    | 18.1 us: 1.01x faster                                      |
| regex_effbot               | 2.58 ms                                                    | 2.56 ms: 1.01x faster                                      |
| pickle_list                | 2.96 us                                                    | 2.93 us: 1.01x faster                                      |
| regex_v8                   | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                      |
| pidigits                   | 282 ms                                                     | 284 ms: 1.01x slower                                       |
| telco                      | 4.60 ms                                                    | 4.63 ms: 1.01x slower                                      |
| xml_etree_parse            | 106 ms                                                     | 107 ms: 1.01x slower                                       |
| json_loads                 | 16.8 us                                                    | 17.1 us: 1.01x slower                                      |
| json                       | 2.93 ms                                                    | 2.99 ms: 1.02x slower                                      |
| unpickle_list              | 2.88 us                                                    | 2.98 us: 1.03x slower                                      |
| dask                       | 221 ms                                                     | 230 ms: 1.04x slower                                       |
| regex_dna                  | 149 ms                                                     | 155 ms: 1.04x slower                                       |
| docutils                   | 1.44 sec                                                   | 1.51 sec: 1.05x slower                                     |
| richards                   | 31.8 ms                                                    | 33.6 ms: 1.05x slower                                      |
| sqlite_synth               | 1.55 us                                                    | 1.64 us: 1.06x slower                                      |
| json_dumps                 | 6.23 ms                                                    | 6.61 ms: 1.06x slower                                      |
| coverage                   | 45.0 ms                                                    | 47.9 ms: 1.06x slower                                      |
| mdp                        | 1.53 sec                                                   | 1.63 sec: 1.07x slower                                     |
| async_generators           | 281 ms                                                     | 301 ms: 1.07x slower                                       |
| richards_super             | 35.2 ms                                                    | 37.7 ms: 1.07x slower                                      |
| tornado_http               | 66.7 ms                                                    | 71.4 ms: 1.07x slower                                      |
| deepcopy_reduce            | 1.82 us                                                    | 1.95 us: 1.07x slower                                      |
| sympy_expand               | 226 ms                                                     | 243 ms: 1.08x slower                                       |
| asyncio_tcp                | 402 ms                                                     | 435 ms: 1.08x slower                                       |
| pathlib                    | 23.3 ms                                                    | 25.3 ms: 1.08x slower                                      |
| dulwich_log                | 27.6 ms                                                    | 30.1 ms: 1.09x slower                                      |
| deepcopy                   | 204 us                                                     | 224 us: 1.10x slower                                       |
| crypto_pyaes               | 49.5 ms                                                    | 54.5 ms: 1.10x slower                                      |
| 2to3                       | 161 ms                                                     | 179 ms: 1.11x slower                                       |
| xml_etree_process          | 37.1 ms                                                    | 41.2 ms: 1.11x slower                                      |
| go                         | 101 ms                                                     | 112 ms: 1.11x slower                                       |
| pycparser                  | 632 ms                                                     | 706 ms: 1.12x slower                                       |
| scimark_sor                | 94.9 ms                                                    | 106 ms: 1.12x slower                                       |
| meteor_contest             | 70.3 ms                                                    | 78.7 ms: 1.12x slower                                      |
| pickle_pure_python         | 179 us                                                     | 201 us: 1.12x slower                                       |
| xml_etree_generate         | 52.7 ms                                                    | 59.6 ms: 1.13x slower                                      |
| sympy_integrate            | 10.3 ms                                                    | 11.7 ms: 1.13x slower                                      |
| xml_etree_iterparse        | 71.5 ms                                                    | 81.1 ms: 1.13x slower                                      |
| sympy_str                  | 131 ms                                                     | 149 ms: 1.14x slower                                       |
| async_tree_cpu_io_mixed    | 467 ms                                                     | 532 ms: 1.14x slower                                       |
| scimark_lu                 | 66.9 ms                                                    | 76.1 ms: 1.14x slower                                      |
| tomli_loads                | 1.47 sec                                                   | 1.67 sec: 1.14x slower                                     |
| sqlglot_transpile          | 891 us                                                     | 1.02 ms: 1.14x slower                                      |
| sqlglot_parse              | 732 us                                                     | 838 us: 1.14x slower                                       |
| sqlglot_normalize          | 166 ms                                                     | 191 ms: 1.15x slower                                       |
| pyflate                    | 321 ms                                                     | 369 ms: 1.15x slower                                       |
| chameleon                  | 4.27 ms                                                    | 4.93 ms: 1.15x slower                                      |
| sympy_sum                  | 69.2 ms                                                    | 80.2 ms: 1.16x slower                                      |
| sqlglot_optimize           | 30.9 ms                                                    | 35.9 ms: 1.16x slower                                      |
| bench_thread_pool          | 447 us                                                     | 523 us: 1.17x slower                                       |
| coroutines                 | 15.8 ms                                                    | 18.6 ms: 1.17x slower                                      |
| logging_format             | 3.31 us                                                    | 3.90 us: 1.18x slower                                      |
| deepcopy_memo              | 22.6 us                                                    | 26.7 us: 1.18x slower                                      |
| logging_simple             | 3.04 us                                                    | 3.60 us: 1.18x slower                                      |
| unpickle_pure_python       | 141 us                                                     | 168 us: 1.19x slower                                       |
| logging_silent             | 60.1 ns                                                    | 72.1 ns: 1.20x slower                                      |
| pprint_safe_repr           | 465 ms                                                     | 561 ms: 1.21x slower                                       |
| async_tree_cpu_io_mixed_tg | 451 ms                                                     | 549 ms: 1.22x slower                                       |
| pprint_pformat             | 947 ms                                                     | 1.15 sec: 1.22x slower                                     |
| generators                 | 22.9 ms                                                    | 28.0 ms: 1.22x slower                                      |
| async_tree_io_tg           | 565 ms                                                     | 703 ms: 1.24x slower                                       |
| regex_compile              | 68.5 ms                                                    | 85.5 ms: 1.25x slower                                      |
| async_tree_none            | 209 ms                                                     | 263 ms: 1.26x slower                                       |
| async_tree_io              | 563 ms                                                     | 719 ms: 1.28x slower                                       |
| fannkuch                   | 248 ms                                                     | 324 ms: 1.30x slower                                       |
| async_tree_memoization     | 260 ms                                                     | 339 ms: 1.31x slower                                       |
| raytrace                   | 147 ms                                                     | 195 ms: 1.32x slower                                       |
| nqueens                    | 52.2 ms                                                    | 69.7 ms: 1.34x slower                                      |
| scimark_fft                | 181 ms                                                     | 246 ms: 1.36x slower                                       |
| scimark_monte_carlo        | 42.5 ms                                                    | 57.9 ms: 1.36x slower                                      |
| mako                       | 6.99 ms                                                    | 9.60 ms: 1.37x slower                                      |
| chaos                      | 34.0 ms                                                    | 47.5 ms: 1.40x slower                                      |
| mypy2                      | 379 ms                                                     | 532 ms: 1.40x slower                                       |
| async_tree_none_tg         | 198 ms                                                     | 277 ms: 1.40x slower                                       |
| float                      | 48.6 ms                                                    | 68.2 ms: 1.40x slower                                      |
| async_tree_memoization_tg  | 240 ms                                                     | 346 ms: 1.45x slower                                       |
| nbody                      | 59.6 ms                                                    | 86.3 ms: 1.45x slower                                      |
| scimark_sparse_mat_mult    | 2.77 ms                                                    | 4.04 ms: 1.46x slower                                      |
| hexiom                     | 4.06 ms                                                    | 6.21 ms: 1.53x slower                                      |
| spectral_norm              | 66.4 ms                                                    | 102 ms: 1.54x slower                                       |
| comprehensions             | 10.2 us                                                    | 15.7 us: 1.55x slower                                      |
| deltablue                  | 2.14 ms                                                    | 3.59 ms: 1.68x slower                                      |
| Geometric mean             | (ref)                                                      | 1.14x slower                                               |

Benchmark hidden because not significant (2): asyncio_websockets, asyncio_tcp_ssl
Ignored benchmarks (18) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (1) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 0.94x