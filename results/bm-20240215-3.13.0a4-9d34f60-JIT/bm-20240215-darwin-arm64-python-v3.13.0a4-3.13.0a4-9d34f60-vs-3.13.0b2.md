# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a4
- machine: darwin-arm64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 190 ms: 1.18x slower                                       |
| chameleon      | 4.27 ms                                                    | 4.81 ms: 1.13x slower                                      |
| docutils       | 1.44 sec                                                   | 1.48 sec: 1.03x slower                                     |
| tornado_http   | 66.7 ms                                                    | 69.6 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                      | 1.09x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 467 ms                                                     | 519 ms: 1.11x slower                                       |
| async_tree_cpu_io_mixed_tg | 451 ms                                                     | 530 ms: 1.18x slower                                       |
| async_tree_io_tg           | 565 ms                                                     | 666 ms: 1.18x slower                                       |
| async_tree_none            | 209 ms                                                     | 252 ms: 1.20x slower                                       |
| async_tree_io              | 563 ms                                                     | 699 ms: 1.24x slower                                       |
| async_tree_memoization     | 260 ms                                                     | 328 ms: 1.26x slower                                       |
| async_tree_none_tg         | 198 ms                                                     | 259 ms: 1.31x slower                                       |
| async_tree_memoization_tg  | 240 ms                                                     | 322 ms: 1.35x slower                                       |
| Geometric mean             | (ref)                                                      | 1.23x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                       |
| float          | 48.6 ms                                                    | 55.5 ms: 1.14x slower                                      |
| nbody          | 59.6 ms                                                    | 75.9 ms: 1.27x slower                                      |
| Geometric mean | (ref)                                                      | 1.13x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.54 ms: 1.02x faster                                      |
| regex_v8       | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                      |
| regex_dna      | 149 ms                                                     | 150 ms: 1.01x slower                                       |
| regex_compile  | 68.5 ms                                                    | 75.1 ms: 1.10x slower                                      |
| Geometric mean | (ref)                                                      | 1.02x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.40 sec: 1.05x faster                                     |
| pickle               | 7.48 us                                                    | 7.33 us: 1.02x faster                                      |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.01x faster                                      |
| json_loads           | 16.8 us                                                    | 16.9 us: 1.00x slower                                      |
| pickle_list          | 2.96 us                                                    | 2.99 us: 1.01x slower                                      |
| json_dumps           | 6.23 ms                                                    | 6.48 ms: 1.04x slower                                      |
| xml_etree_process    | 37.1 ms                                                    | 38.7 ms: 1.05x slower                                      |
| xml_etree_iterparse  | 71.5 ms                                                    | 74.8 ms: 1.05x slower                                      |
| xml_etree_generate   | 52.7 ms                                                    | 56.1 ms: 1.06x slower                                      |
| unpickle_list        | 2.88 us                                                    | 3.10 us: 1.07x slower                                      |
| pickle_pure_python   | 179 us                                                     | 196 us: 1.10x slower                                       |
| unpickle_pure_python | 141 us                                                     | 158 us: 1.12x slower                                       |
| Geometric mean       | (ref)                                                      | 1.03x slower                                               |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 13.1 ms: 1.16x faster                                      |
| python_startup_no_site | 12.3 ms                                                    | 11.6 ms: 1.07x faster                                      |
| Geometric mean         | (ref)                                                      | 1.11x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 6.99 ms                                                    | 7.79 ms: 1.12x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 897 us                                                     | 705 us: 1.27x faster                                       |
| typing_runtime_protocols   | 87.6 us                                                    | 70.9 us: 1.23x faster                                      |
| python_startup             | 15.2 ms                                                    | 13.1 ms: 1.16x faster                                      |
| python_startup_no_site     | 12.3 ms                                                    | 11.6 ms: 1.07x faster                                      |
| tomli_loads                | 1.47 sec                                                   | 1.40 sec: 1.05x faster                                     |
| bench_mp_pool              | 47.2 ms                                                    | 45.9 ms: 1.03x faster                                      |
| gc_traversal               | 2.45 ms                                                    | 2.39 ms: 1.02x faster                                      |
| telco                      | 4.60 ms                                                    | 4.51 ms: 1.02x faster                                      |
| pickle                     | 7.48 us                                                    | 7.33 us: 1.02x faster                                      |
| regex_effbot               | 2.58 ms                                                    | 2.54 ms: 1.02x faster                                      |
| crypto_pyaes               | 49.5 ms                                                    | 49.1 ms: 1.01x faster                                      |
| pickle_dict                | 18.3 us                                                    | 18.2 us: 1.01x faster                                      |
| pidigits                   | 282 ms                                                     | 283 ms: 1.00x slower                                       |
| richards                   | 31.8 ms                                                    | 31.9 ms: 1.00x slower                                      |
| json_loads                 | 16.8 us                                                    | 16.9 us: 1.00x slower                                      |
| json                       | 2.93 ms                                                    | 2.95 ms: 1.01x slower                                      |
| regex_v8                   | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                      |
| regex_dna                  | 149 ms                                                     | 150 ms: 1.01x slower                                       |
| pickle_list                | 2.96 us                                                    | 2.99 us: 1.01x slower                                      |
| richards_super             | 35.2 ms                                                    | 35.7 ms: 1.01x slower                                      |
| pyflate                    | 321 ms                                                     | 326 ms: 1.02x slower                                       |
| sqlite_synth               | 1.55 us                                                    | 1.59 us: 1.03x slower                                      |
| docutils                   | 1.44 sec                                                   | 1.48 sec: 1.03x slower                                     |
| json_dumps                 | 6.23 ms                                                    | 6.48 ms: 1.04x slower                                      |
| tornado_http               | 66.7 ms                                                    | 69.6 ms: 1.04x slower                                      |
| xml_etree_process          | 37.1 ms                                                    | 38.7 ms: 1.05x slower                                      |
| xml_etree_iterparse        | 71.5 ms                                                    | 74.8 ms: 1.05x slower                                      |
| mdp                        | 1.53 sec                                                   | 1.61 sec: 1.05x slower                                     |
| coverage                   | 45.0 ms                                                    | 47.5 ms: 1.06x slower                                      |
| meteor_contest             | 70.3 ms                                                    | 74.3 ms: 1.06x slower                                      |
| xml_etree_generate         | 52.7 ms                                                    | 56.1 ms: 1.06x slower                                      |
| sympy_expand               | 226 ms                                                     | 241 ms: 1.07x slower                                       |
| sympy_integrate            | 10.3 ms                                                    | 11.1 ms: 1.07x slower                                      |
| sympy_str                  | 131 ms                                                     | 141 ms: 1.07x slower                                       |
| fannkuch                   | 248 ms                                                     | 267 ms: 1.07x slower                                       |
| unpickle_list              | 2.88 us                                                    | 3.10 us: 1.07x slower                                      |
| sqlglot_parse              | 732 us                                                     | 787 us: 1.08x slower                                       |
| async_generators           | 281 ms                                                     | 303 ms: 1.08x slower                                       |
| dulwich_log                | 27.6 ms                                                    | 29.8 ms: 1.08x slower                                      |
| pathlib                    | 23.3 ms                                                    | 25.4 ms: 1.09x slower                                      |
| sympy_sum                  | 69.2 ms                                                    | 75.3 ms: 1.09x slower                                      |
| deepcopy_reduce            | 1.82 us                                                    | 1.98 us: 1.09x slower                                      |
| sqlglot_transpile          | 891 us                                                     | 973 us: 1.09x slower                                       |
| go                         | 101 ms                                                     | 110 ms: 1.10x slower                                       |
| regex_compile              | 68.5 ms                                                    | 75.1 ms: 1.10x slower                                      |
| pycparser                  | 632 ms                                                     | 693 ms: 1.10x slower                                       |
| pickle_pure_python         | 179 us                                                     | 196 us: 1.10x slower                                       |
| sqlglot_normalize          | 166 ms                                                     | 182 ms: 1.10x slower                                       |
| pprint_pformat             | 947 ms                                                     | 1.05 sec: 1.11x slower                                     |
| deepcopy                   | 204 us                                                     | 226 us: 1.11x slower                                       |
| pprint_safe_repr           | 465 ms                                                     | 515 ms: 1.11x slower                                       |
| async_tree_cpu_io_mixed    | 467 ms                                                     | 519 ms: 1.11x slower                                       |
| scimark_sor                | 94.9 ms                                                    | 106 ms: 1.11x slower                                       |
| sqlglot_optimize           | 30.9 ms                                                    | 34.4 ms: 1.11x slower                                      |
| mako                       | 6.99 ms                                                    | 7.79 ms: 1.12x slower                                      |
| scimark_lu                 | 66.9 ms                                                    | 74.8 ms: 1.12x slower                                      |
| unpickle_pure_python       | 141 us                                                     | 158 us: 1.12x slower                                       |
| chameleon                  | 4.27 ms                                                    | 4.81 ms: 1.13x slower                                      |
| bench_thread_pool          | 447 us                                                     | 504 us: 1.13x slower                                       |
| logging_simple             | 3.04 us                                                    | 3.45 us: 1.13x slower                                      |
| logging_format             | 3.31 us                                                    | 3.76 us: 1.14x slower                                      |
| float                      | 48.6 ms                                                    | 55.5 ms: 1.14x slower                                      |
| scimark_monte_carlo        | 42.5 ms                                                    | 48.5 ms: 1.14x slower                                      |
| deltablue                  | 2.14 ms                                                    | 2.45 ms: 1.15x slower                                      |
| deepcopy_memo              | 22.6 us                                                    | 26.3 us: 1.16x slower                                      |
| logging_silent             | 60.1 ns                                                    | 70.3 ns: 1.17x slower                                      |
| async_tree_cpu_io_mixed_tg | 451 ms                                                     | 530 ms: 1.18x slower                                       |
| scimark_fft                | 181 ms                                                     | 213 ms: 1.18x slower                                       |
| async_tree_io_tg           | 565 ms                                                     | 666 ms: 1.18x slower                                       |
| nqueens                    | 52.2 ms                                                    | 61.6 ms: 1.18x slower                                      |
| 2to3                       | 161 ms                                                     | 190 ms: 1.18x slower                                       |
| coroutines                 | 15.8 ms                                                    | 18.7 ms: 1.18x slower                                      |
| spectral_norm              | 66.4 ms                                                    | 78.8 ms: 1.19x slower                                      |
| scimark_sparse_mat_mult    | 2.77 ms                                                    | 3.31 ms: 1.19x slower                                      |
| raytrace                   | 147 ms                                                     | 176 ms: 1.20x slower                                       |
| async_tree_none            | 209 ms                                                     | 252 ms: 1.20x slower                                       |
| chaos                      | 34.0 ms                                                    | 41.0 ms: 1.21x slower                                      |
| hexiom                     | 4.06 ms                                                    | 4.91 ms: 1.21x slower                                      |
| generators                 | 22.9 ms                                                    | 28.3 ms: 1.24x slower                                      |
| comprehensions             | 10.2 us                                                    | 12.6 us: 1.24x slower                                      |
| async_tree_io              | 563 ms                                                     | 699 ms: 1.24x slower                                       |
| async_tree_memoization     | 260 ms                                                     | 328 ms: 1.26x slower                                       |
| nbody                      | 59.6 ms                                                    | 75.9 ms: 1.27x slower                                      |
| async_tree_none_tg         | 198 ms                                                     | 259 ms: 1.31x slower                                       |
| async_tree_memoization_tg  | 240 ms                                                     | 322 ms: 1.35x slower                                       |
| dask                       | 221 ms                                                     | 335 ms: 1.51x slower                                       |
| mypy2                      | 379 ms                                                     | 577 ms: 1.52x slower                                       |
| Geometric mean             | (ref)                                                      | 1.09x slower                                               |

Benchmark hidden because not significant (5): asyncio_tcp, xml_etree_parse, asyncio_websockets, unpickle, asyncio_tcp_ssl
Ignored benchmarks (18) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (1) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.07x